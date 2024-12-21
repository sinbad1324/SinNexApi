from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from modules.Purchased.getUserPluginList import GetPluginList, FundSinNex
from modules.session.createSession import NewSession, FindValideSession, DeletSession
import modules.AddUser as add
import modules.ImagesAPI.core as Core
import modules.api.Security.verifyApi as sec

# import Data.postgresql.auth as sql
import modules.obfuscator.ToluaOfs as ob
import modules.api.Security.decrypt as security
import modules.obfuscator.luaCode as obfCode
import modules.Robloxplugin.Graph as graph
from modules.colorGenerator.color import GenerateColor, random  

ports = os.environ.get("PORT") or 5000
def ValideUser(header, record):
    if not sec.VerifieHeader(header):
        return jsonify(
            {
                "message": "Your header is not accepted!",
                "error": "header",
                "succ": False,
            }
        )
    if not sec.VerifieRobloxUser(str(record["userId"])):
        return jsonify(
            {
                "message": "Your information is incorrect!",
                "error": "Roblox user",
                "succ": False,
            }
        )
    if not security.VerifiePassword(header.get("password"), record["userId"]):
        return jsonify(
            {
                "message": "Your api keys are not right!",
                "error": "Api key",
                "succ": False,
            }
        )
    return True


app = Flask(__name__)
CORS(app)


@app.route("/")
def htmlPage():
    ip_addr = request.remote_addr
    return "<h1> Your IP address is:" + ip_addr + " Aleksandre"


@app.route("/api/getAllInfos", methods=["POST"])
def GetAllInfos():
    try:
        record = request.get_json()
        header = request.headers
        valideSession = FindValideSession(
            str(record["userId"]), str(request.remote_addr), str(record["sessionId"])
        )
        if (
            valideSession != None
            and type(valideSession) is dict
            or valideSession == False
        ):
            return jsonify(valideSession)
        validation = ValideUser(header, record)
        if add.UserExist(str(record["userId"])) == None:
            return jsonify(
                {"message": "You are not logged in!", "error": "login", "succ": False}
            )
        if type(validation) is dict:
            return validation
        if "methode" in record and record["methode"] == "strict":
            return jsonify(Core.GetAll(record["Assets"], "strict"))
        else:
            return jsonify(Core.GetAll(record["Assets"]))
    except ValueError as e:
        print(e)
    return "[]"


@app.route("/api/obfucate", methods=["POST"])
def obfus():
    try:
        record = request.get_json()
        header = request.headers
        valideSession = FindValideSession(
            str(record["userId"]), str(request.remote_addr), str(record["sessionId"])
        )
        if (
            valideSession != None
            and type(valideSession) is dict
            or valideSession == False
        ):
            return jsonify(valideSession)
        validation = ValideUser(header, record)
        if type(validation) is dict:
            return validation
        if add.UserExist(str(record["userId"])) == None:
            return jsonify(
                {"message": "You are not logged in!", "error": "login", "succ": False}
            )

        return ob.getObfuscedCode(obfCode.GetCode(record["gameId"]))
    except ValueError as e:
        return jsonify({"message": e, "succ": False})


@app.route("/api/login", methods=["POST"])
def Loign():
    try:
        record = request.get_json()
        header = request.headers
        if not sec.VerifieRobloxUser(str(record["userId"])):
            return jsonify(
                {
                    "message": "Your information is incorrect!",
                    "error": "Roblox user",
                    "succ": False,
                }
            )
        if not sec.VerifieHeader(header):
            return jsonify(
                {
                    "message": "Your header is not accepted!",
                    "error": "header",
                    "succ": False,
                }
            )
        if not security.decrypt(header.get("password"), record["userId"]):
            return jsonify(
                {
                    "message": "Your api keys are not right!",
                    "error": "Api key",
                    "succ": False,
                }
            )
        value, data = GetPluginList(str(record["userId"]))
        if not value:
            return jsonify({"message": data["message"], "succ": False})
        if FundSinNex(data):
            if add.UserExist(str(record["userId"])):
                return jsonify({"message": "Can't add this user", "succ": False})
            else:
                add.AddNewUser(str(record["userId"]))
                return jsonify({"message": "User Added", "succ": True})
        else:
            return jsonify(
                {
                    "message": "Don't be stingy buy the plugin. :D",
                    "error": "Plugin",
                    "succ": False,
                }
            )
    except ValueError as e:
        print(e)
    return jsonify({"message": "Can't connecte", "succ": False})


@app.route("/api/connecting", methods=["POST"])
def Connecting():
    try:
        record = json.loads(request.get_data(cache=True, parse_form_data=True))
        header = request.headers
        if not add.UserExist(str(record["userId"])):
            return jsonify(
                {"message": "You are not logged in!", "error": "login", "succ": False}
            )
        validation = ValideUser(header, record)
        if type(validation) is dict:
            return validation
        value, data = GetPluginList(str(record["userId"]))
        if not value:
            return jsonify({"message": data["message"], "succ": False})
        else:
            if FundSinNex(data):
                if "Force" in record and record["Force"] == True:
                    DeletSession(str(record["userId"]))
                sessionId = NewSession(str(record["userId"]), str(request.remote_addr))
                if type(sessionId) is dict:
                    return jsonify(sessionId)
                else:
                    return jsonify(
                        {"message": "Connected", "sessionId": sessionId, "succ": True}
                    )
            else:
                return jsonify(
                    {
                        "message": "Buy the pls plugin to use it!",
                        "error": "Ban!",
                        "succ": False,
                    }
                )
    except ValueError as e:
        print(e)
        return jsonify({"message": str(e), "succ": False})


@app.route("/api/converToSq", methods=["POST"])
def ConverToSq():
    try:
        record = request.get_json()
        header = request.headers
        seq = 16
        if "seq" in record and record["seq"] >= 2 and record["seq"] <= 16:
            seq = record["seq"]
        env = 0
        if "env" in record:
            env = record["env"]
        point = []
        if "points" in record:
            point = record["points"]
        valideSession = FindValideSession(
            str(record["userId"]), str(request.remote_addr), str(record["sessionId"])
        )
        if (
            valideSession != None
            and type(valideSession) is dict
            or valideSession == False
        ):
            return jsonify(valideSession)
        validation = ValideUser(header, record)
        if type(validation) is dict:
            return validation
        if add.UserExist(str(record["userId"])) == None:
            return jsonify(
                {"message": "You are not logged in!", "error": "login", "succ": False}
            )
        return jsonify(
            {"succ": True, "data": graph.convert_to_number_sequence(point, seq, env)}
        )
    except ValueError as e:
        return jsonify({"message": e, "succ": False})


@app.route("/api/getGraphData", methods=["POST"])
def GetGraphData():
    try:
        record = request.get_json()
        header = request.headers
        valideSession = FindValideSession(
            str(record["userId"]), str(request.remote_addr), str(record["sessionId"])
        )
        if (
            valideSession != None
            and type(valideSession) is dict
            or valideSession == False
        ):
            return jsonify(valideSession)
        validation = ValideUser(header, record)
        if type(validation) is dict:
            return validation
        if add.UserExist(str(record["userId"])) == None:
            return jsonify(
                {"message": "You are not logged in!", "error": "login", "succ": False}
            )
        if "data" in record:
            print(record["data"])
            default_names, default_curves = graph.get_data(record["data"])
            return jsonify(
                {
                    "succ": True,
                    "data": {
                        "default_names": default_names,
                        "default_curves": default_curves,
                    },
                }
            )
        return jsonify({"succ": False, "data": {}})
    except ValueError as e:
        return jsonify({"message": str(e), "succ": False})


@app.route("/api/colorGenerator", methods=["POST"])
def GetRandomColor():
    try:
        record = request.get_json()
        header = request.headers
        valideSession = FindValideSession(
            str(record["userId"]), str(request.remote_addr), str(record["sessionId"])
        )
        if (
            valideSession != None
            and type(valideSession) is dict
            or valideSession == False
        ):
            return jsonify(valideSession)
        validation = ValideUser(header, record)
        if type(validation) is dict:
            return validation
        if add.UserExist(str(record["userId"])) == None:
            return jsonify(
                {"message": "You are not logged in!", "error": "login", "succ": False}
            )
        points = 0
        if "sequence" in record:
            points = record["sequence"]
        return jsonify({"data":GenerateColor(points) , "succ":True})
    except ValueError as e:
        return jsonify({"message": str(e), "succ": False})


if __name__ == "__main__":
    print("falsk")
    app.run(host="0.0.0.0", port=5000)



# def AddNewUser(con , cur):
#     cur.execute(f"SELECT * FROM Users WHERE userID ={record["userId"]}")
#     user = cur.fetchone()
#     if user is None:
#         cur.execute(f"INSERT INTO Users(userID) VALUES ({record["userId"]});")
#         con.commit()
#         return "User Created"
#     else:
#         return "User Exist"

# return sql.aut(AddNewUser)

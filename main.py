import json
from flask import Flask , request ,jsonify
from flask_cors import CORS
import modules.AddUser as add
import modules.ImagesAPI.core as Core
import modules.api.Security.verifyApi as sec
import Data.postgresql.auth as sql
import modules.obfuscator.ToluaOfs as ob


app = Flask(__name__)
CORS(app)
@app.route("/")
def htmlPage():
    return "<h1>Hello , world</h1>"

@app.route("/GetAllInfos" , methods=['POST'])
def GetAllInfos():
    try:
        record =  json.loads(request.data)     
        header = request.headers
        if  sec.VerifieHeader(header) and sec.VerifieRobloxUser(str(record["userId"])) and add.UserExist(str(record["userId"])):
            return json.dumps(Core.GetAll(record["Assets"]))
    except ValueError as e:
        return "[]"


@app.route("/Obfucate" , methods=["POST"])
def obfus():
    try:
        record =  json.loads(request.data)     
        header = request.headers
        if  sec.VerifieHeader(header) and sec.VerifieRobloxUser(str(record["userId"])) and add.UserExist(str(record["userId"])):
           if record["code"]:
                return ob.getObfuscedCode(record["code"])
           else:
               return "[code:warn('No code.')]"
    except ValueError as e:
        return "[]"



@app.route("/login" , methods=["POST"] )
def Loign():
    try:
        record =  json.loads(request.data)     
        header = request.headers
        if sec.VerifieHeader(header) and sec.VerifieRobloxUser(str(record["userId"])):   
            if add.UserExist(str(record["userId"])):
                return json.dumps({"message":"User Existe"})
            else:
                add.AddNewUser(str(record["userId"]))
                return  json.dumps({"message":"User Added"})
    except ValueError as e:
        print(e)
    return "FALSE"


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

@app.route("/Connecting" , methods=["POST"] )
def Connecting():
    try:
        record =  json.loads(request.data)     
        header = request.headers
        if sec.VerifieHeader(header) and sec.VerifieRobloxUser(str(record["userId"])) and add.UserExist(record["userId"]): 
                return 
    except ValueError as e:
        print(e)
    return "FALSE"


if __name__ == "__main__":
    print("true")
    app.run(debug=True,port=5000,use_reloader=True)


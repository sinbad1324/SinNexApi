import json
from flask import Flask , request ,jsonify
from flask_cors import CORS
import modules.AddUser as add
import modules.ImagesAPI.core as Core
import modules.api.Security.verifyApi as sec
#import Data.postgresql.auth as sql
import modules.obfuscator.ToluaOfs as ob
import modules.api.Security.decrypt as security

def ValideUser(header,record):
    return  sec.VerifieHeader(header) and sec.VerifieRobloxUser(str(record["userId"])) and security.VerifiePassword(header.get("password"),record["userId"])

app = Flask(__name__)
CORS(app)

@app.route("/")
def htmlPage():
    ip_addr = request.remote_addr
    return '<h1> Your IP address is:' + ip_addr

@app.route("/GetAllInfos" , methods=['POST'])
def GetAllInfos():
    try:
        record =  json.loads(request.data)     
        header = request.headers
        if ValideUser(header,record) and add.UserExist(str(record["userId"])):
            if "methode" in record and record["methode"] == "strict":
                return json.dumps(Core.GetAll(record["Assets"] , "strict"))
            else :
                return json.dumps(Core.GetAll(record["Assets"]))
    except ValueError as e:
        print(e)
    return "[]"


@app.route("/Obfucate" , methods=["POST"])
def obfus():
    try:
        record =  json.loads(request.data)     
        header = request.headers
        if ValideUser(header,record) and add.UserExist(str(record["userId"])):
           if record["code"]:
                return ob.getObfuscedCode(record["code"])
           else:
            return json.dumps({"message":"Where is the code ?" , "succ":False ,"code":"warn('No code.')" })

    except ValueError as e:
        return json.dumps({"message":e , "succ":False})



@app.route("/login" , methods=["POST"] )
def Loign():
    try:
        record =  json.loads(request.data)     
        header = request.headers 
        if  sec.VerifieHeader(header) and sec.VerifieRobloxUser(str(record["userId"])) and security.decrypt(header.get("password"),record["userId"]):
            if add.UserExist(str(record["userId"])):
                return json.dumps({"message":"User Existe"})
            else:
                add.AddNewUser(str(record["userId"]))
                return  json.dumps({"message":"User Added"})
    except ValueError as e:
        print(e)
    return json.dumps({"message":"Can't connecte" , "succ":False})



@app.route("/Connecting" , methods=["POST"] )
def Connecting():
    try:
        record =  json.loads(request.data)     
        header = request.headers
        print(ValideUser(header,record) and add.UserExist(str(record["userId"])) != None)
        if ValideUser(header,record) and add.UserExist(str(record["userId"])) != None:
            return json.dumps({"message":"Connected" , "succ":True})
    except ValueError as e:
        print(e)
    return json.dumps({"message":"Can't connecte" , "succ":False})


if __name__ == "__main__":
    print("true")
    app.run(debug=True,port=5000,use_reloader=True)






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

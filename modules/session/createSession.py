from modules.AddUser import addNewValueOnUser , GetUser , DeletetheOne
from modules.randomChar import randomString
import time
from math import floor
def NewSession(userId:str , ipAdresse:str):
    x,user = GetUser(userId)
    def createData():
        sessionId = randomString(20)
        addNewValueOnUser(userId , "SessionData" ,  {
            "datetime": floor(time.time()),
            "sessionId":sessionId,
            "ipAdresse":ipAdresse
        }) 
        return sessionId

    if user:
        if not "SessionData" in user:
          return createData()    
        else:
            if (floor(time.time()) - user["SessionData"]["datetime"]) >= (24 * 60 * 60):
                return createData()
            else: return {"message":"Your session is over!" ,"error":"Time" ,"succ":False}
    return {"message":"You are not logged in!" ,"error":"login","succ":False}

def FindValideSession(userId:str , ipAdresse:str , sessionId:str):
    x, user = GetUser(userId)
    if user and  "SessionData" in user:
        data = user["SessionData"]
        if data:
            if ((floor(time.time())- user["SessionData"]["datetime"])  <= (24 * 60 * 60)) :
                if  data["ipAdresse"] != ipAdresse:
                    return {"message":"Your IP address is invalid!","error":"ipAdresse" , "succ":False}  
                if data["sessionId"] != sessionId:
                    return {"message":"Your session key is invalid","error":"sessionId" , "succ":False}  
                return True
            else:
                return {"message":"Your session is no longer valid, recreate another session!","error":"Session Time" , "succ":False}  
    return False

def DeletSession(userId:str):
    DeletetheOne(userId , "SessionData")
    
    
    


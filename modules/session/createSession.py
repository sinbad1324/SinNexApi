import AddUser as userC
from randomChar import randomString
from datetime import datetime
date_format = '%Y-%m-%d %H:%M:%S'

def NewSession(userId:str , ipAdresse:str):
    userC.addNewValueOnUser(userId , randomString(20)) #pos 2
    userC.addNewValueOnUser(userId , datetime.now().strftime(date_format)) #pos 3
    userC.addNewValueOnUser(userId , ipAdresse) # pos 4


def FindValideSession(userId:str , ipAdresse:str , sessionId:str):
    user = userC.GetUser(userId)
    if user and len(user)>= 5:
        if user[3]:
            date:datetime = datetime.strptime(user[3] , date_format)
            if ((date - datetime. datetime(1970, 1, 1)) <= (24*60*60)) and user[2] == sessionId and user[4] == ipAdresse:
                return True
    return False
                
            
            
        
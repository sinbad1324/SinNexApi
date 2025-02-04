import re
import math
from modules.AddUser  import  UserExist , addNewValueOnUser ,DeletetheOne

def decrypt(key:str , userID:int) -> bool:
    newText = re.sub(r"[\@\!\#\_]", lambda m: {'@': '(', '#': ')', '!': '(', '_': ')'}[m.group(0)], key)
    formul = re.sub(r"[^0-9\(\)\+\-\*/\^]", "", newText)
    result = math.floor(eval(formul))
    result = (result - math.floor(userID/100-23))
    if  result < 10 and result > -10 :
        return True
    return False


def VerifiePassword(key:str , userID:int)-> bool:
    user = UserExist(str(userID))
    if not user :
        return False
    decrypted =decrypt(key , userID)
    if  decrypted  and  not "password" in user or  user["password"] != key:
        DeletetheOne(str(userID) ,"password")
        addNewValueOnUser(str(userID) ,"password", key) 
        return decrypted
    return True

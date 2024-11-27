import modules.Json as js
from cryptography.fernet import Fernet

file:str = "JSON/Users"

def AddNewUser(user:str):
    try:
        li:list = js.Read( file, [])
        if len(li)>0:
            key:str = li[0][0]
            key = key.encode()
            if key :
                fernet = Fernet(key)
                cryp =fernet.encrypt(user.encode())
                js.AddJSON(value=[cryp.decode("utf-8")] , file=file)
            else:
                js.AddJSON(value=[Fernet.generate_key().decode("utf-8") , "@@AboMet7557601GKgNfGdBz^xhTAKrD1KfpRAkFE_+wEYK$A9cgGNXlsDzD_"] , file=file)
                AddNewUser(user)
        else:
            js.AddJSON(value=[Fernet.generate_key().decode("utf-8") , "@@AboMet7557601GKgNfGdBz^xhTAKrD1KfpRAkFE_+wEYK$A9cgGNXlsDzD_"] , file=file)
            AddNewUser(user)
    except IndexError as e:
        print(e) 

def GetUser(user:str) ->tuple[list , list[str]]:
    li:list[str] = js.Read( file, [])
    if len(li)>0:
        key:str = li[0][0]
        key = key.encode()
        fernet = Fernet(key)
        for i in range(len(li)):
            if i > 0:
                usertab:list[str] =li[i]
                return li , usertab
    return li , False


def UserExist(user:str):   
    li, usertab= GetUser(user)
    return usertab



def addNewValueOnUser(user:str ,value):
    try:
        li, usertab= GetUser(user)
        usertab.append(value)
        js.Write( li, file)
    except IndexError as e:
        print(e)

def DeletetheOne(user):
    try:
        li, usertab= GetUser(user)
        if (len(usertab)-1) >= 1:
            usertab.pop()
        js.Write( li, file)
    except IndexError as e:
        print(e)

# crypedmess = AddNewUser("35322342")
# fernet = Fernet(key)

# print(fernet.decrypt(crypedmess))

#AddNewUser("1232424242")

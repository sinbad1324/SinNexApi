import modules.Json as js
from cryptography.fernet import Fernet

file:str = "JSON/Users"

def AddNewUser(user:str):
    try:
        li:list = js.Read( file, [])
        if len(li)>0:
            key:str = li[0]
            key = key.encode()
            if key :
                fernet = Fernet(key)
                cryp =fernet.encrypt(user.encode())
                js.AddJSON(value=cryp.decode("utf-8") , file=file)
            else:
                js.AddJSON(value=Fernet.generate_key().decode("utf-8") , file=file)
                AddNewUser(user)
        else:
            js.AddJSON(value=Fernet.generate_key().decode("utf-8") , file=file)
            AddNewUser(user)
    except IndexError as e:
        print(e) 

def UserExist(user:str):   
    try:
        li:list[str] = js.Read( file, [])
        if len(li)>0:
            key:str = li[0]
            key = key.encode()
            fernet = Fernet(key)
            for i in range(len(li)):
                if i > 0:
                    if fernet.decrypt(li[i]).decode()  == user:
                        return True
        return False
                
    except IndexError as e:
        print(e) 

# crypedmess = AddNewUser("35322342")
# fernet = Fernet(key)

# print(fernet.decrypt(crypedmess))


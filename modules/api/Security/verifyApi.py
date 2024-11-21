import requests
import secret.keys as secret

def VerifieRobloxUser(id:str)->bool:
    req = requests.get("https://users.roblox.com/v1/users/"+id)
    respons:dict = req.json()
    _id = respons.get("id")
    if  _id and str(_id) == id :
        return True
    return False

def VerifieHeader(header:dict):
    if VerifieKey(header.get("Apikey")) and header.get("User-Agent").find("RobloxStudio/WinInet") >= 0 and header.get("Roblox-Id"):
        return True
    return False


def VerifieKey(key)->bool:
    return secret.api_key == key




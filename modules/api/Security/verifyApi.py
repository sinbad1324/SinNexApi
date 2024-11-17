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
    print(VerifieKey(header.get("Apikey")))
    print( header.get("User-Agent") == "RobloxStudio/WinInet RobloxApp/0.651.0.6510833 (GlobalDist; RobloxDirectDownload)" )
    print(VerifieRobloxUser(header.get("Roblox-Id")))
    if VerifieKey(header.get("Apikey")) and header.get("User-Agent") == "RobloxStudio/WinInet RobloxApp/0.651.0.6510833 (GlobalDist; RobloxDirectDownload)" and header.get("Roblox-Id"):
        return True
    return False


def VerifieKey(key)->bool:
    return secret.api_key == key
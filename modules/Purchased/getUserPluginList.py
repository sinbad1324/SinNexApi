import requests



def GetPluginList(userID:str , cursor=""):
    url:str = "https://inventory.roblox.com/v2/users/"+userID+"/inventory?"
    params = {
        "assetTypes":"Plugin",
        "limit":100,
        "sortOrder":"Desc",
        "cursor":cursor
    }

    for name,value in params:
        url = name+"="+value+"&"

    print(url)

print(GetPluginList())
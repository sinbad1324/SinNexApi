import requests

def GetPluginList(userID:str ,baseData:list[str]=[], cursor=""):
    url:str = "https://inventory.roblox.com/v2/users/"+userID+"/inventory?"
    params = {
        "assetTypes":"Plugin",
        "limit":100,
        "sortOrder":"Desc",
        "cursor":cursor
    }

    for k in params.keys():
        url =url+k+"="+str(params[k])+"&"
    response = requests.get(url)
    response = response.json()
    if "data" in response:
        baseData.extend(response["data"])
        if response["nextPageCursor"] != None:
            return GetPluginList(userID , baseData , response["nextPageCursor"])
    elif "errors" in response:
        if response["errors"][0]["code"] == 4: 
            return False , {"message":"To use this api, set up your public adventaire"}
        else:  return False , {"message":"There was an error wanted you to sit down afterwards"}
    return True, baseData

SinNexId = ""

def FundSinNex(data:list[str]):
    for item in data:
        if "assetId" in item:
            if str(item["assetId"])  == SinNexId:
                return True
    return False


# auth , data = GetPluginList(userID)
# if auth:
#     print(FundSinNex(data))
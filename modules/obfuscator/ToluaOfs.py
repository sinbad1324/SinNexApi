import requests
import json
apiKey = "1f999029-d736-2f3a-b2e4-b232df365a20d3b"

sessionUrl = "https://luaobfuscator.com/api/obfuscator/newscript"
urlObfuscate = "https://luaobfuscator.com/api/obfuscator/obfuscate"
header1= {
    "content-type": "application/json",
    "apikey": apiKey
}
options = {
        "MinifyAll": True,
        "Virtualize": True,
        "CustomPlugins": {
                
        }
}

def  getObfuscedCode(Code):
    getSession = requests.post(sessionUrl , headers=header1 ,  data= Code)
    getSessionRespons = getSession.json()
    sessionId = getSessionRespons["sessionId"]
    if sessionId:
        getcode = requests.post(
            urlObfuscate , 
            headers={
            "content-type": "application/json",
            "apikey": apiKey,
            "sessionId": sessionId
        } ,
        json=options)
        return getcode.json()

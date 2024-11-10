
import json
from flask import Flask , request ,jsonify
from flask_cors import CORS


from modules.PixelImg import Img
from modules.Template import Temp
from modules.Grid import Ggrid
from modules.Files import FilesList
import modules.Json as dt
import modules.ToLua as LU






def Main(path):

    try:
        print(path , "--------------------------Path")
        newimg = Img(path )
        cat = newimg.getCompare()
        NewTemp = Temp(newimg)
        GetGrid = Ggrid(NewTemp) 
        #GetGrid.SetDev(True)
        GetGrid.GetGridTemplate()
        
        FlipBook = GetGrid.GetResult() 
        Size = newimg.GetImgSize() 
    #  newimg.Show(True)
        return FlipBook , Size , newimg.OriginaleID , cat
    except :
        print("No stop here!!!!!!!!!")
    
    return False , False, False , None

#print(Main("110761450786278"))

JSONdict = {}
for img in dt.Read("Assets"):
    flip , size , id  , cat=  Main(img)
    if flip and size and id and cat :
        if cat not in JSONdict:
            JSONdict[cat] ={"Assets":[]}
        JSONdict[cat]["Assets"].append({
            "name": "none",
            "AssetID": id,
            "Flipbook": flip,
            "Size": {
                "x": size["x"],
                "y": size["y"]
            }
        })

# LU.Lua(JSONdict , "LuaU-03-11-2024") 
print(JSONdict)
dt.Write(JSONdict , "FOLDER-TO-PLUGIN/newLua-03-11-2024")
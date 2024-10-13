
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


    print(path , "--------------------------Path")
    newimg = Img(path )

    NewTemp = Temp(newimg)
    GetGrid = Ggrid(NewTemp) 
    #GetGrid.SetDev(True)
    GetGrid.GetGridTemplate()
    
    FlipBook = GetGrid.GetResult() 
    Size = newimg.GetImgSize() 
  #  newimg.Show(True)
    return FlipBook , Size , newimg.OriginaleID

#print(Main("110761450786278"))

JSONdict = []
for img in dt.Read("Assets"):
    flip , size , id =  Main(img)
    JSONdict.append({
        "name": "none",
        "AssetID": id,
        "FlipBook": flip,
        "Sizes": {
            "x": size["x"],
            "y": size["y"]
        }
    })

LU.Lua(JSONdict , "MyLulu_Max_65")
dt.Write(JSONdict , "newLua-13-10-2024")
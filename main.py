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
    #newimg.Show(True)
    return FlipBook , Size , newimg.OriginaleID

#print(Main("18617720196"))


#18617780939 --> mauvais pixelisation


app = Flask(__name__)
CORS(app)
@app.route("/")
def Hello():
    return "Hello ,World"

@app.route("/GetSize")
def GetSize():
    AssetID:str = request.args.get("AssetID") 
    if not AssetID : return "Error: you have to post an ID!"
    newimg = Img(AssetID )
    Size = newimg.GetImgSize() 
    return jsonify({"Size" : Size, "OriginalAssetID":newimg.OriginaleID })



@app.route("/GetOriginal")
def GetOriginal():
    AssetID:str = request.args.get("AssetID") 
    if not AssetID : return "Error: you have to post an ID!"
    newimg = Img(AssetID )
    return jsonify({"AssetID":newimg.OriginaleID })

@app.route("/GetFlipbook")
def GetFlipbook():
    AssetID:str = request.args.get("AssetID") 
    if not AssetID : return "Error: you have to post an ID!"
    newimg = Img(AssetID )
    NewTemp = Temp(newimg)
    GetGrid = Ggrid(NewTemp) 
    #GetGrid.SetDev(True)
    GetGrid.GetGridTemplate()
    
    FlipBook = GetGrid.GetResult() 
    return jsonify({"FlipBook":FlipBook})


@app.route("/GetInfos")
def GetInfos():
    AssetID:str = request.args.get("AssetID") 
    if not AssetID : return "Error: you have to post an ID!"
    FlipBook , Size , asseteID = Main(AssetID)
    return jsonify({{
        "AssetID":asseteID,
        "FlipBook":FlipBook,
        "Size":Size,
    }})


@app.route("/GetSizes" , methods=['POST'])
def GetSizes():
    record:[str] = json.loads(request.data)
    if not record or len(record) < 0 and type(record) != list: return "Not"
    NewData = []
    for AssetID in record:
        newimg = Img(AssetID )
        Size = newimg.GetImgSize()       
        NewData.append(Size)
    return jsonify(NewData)


@app.route("/GetAllInfos" , methods=['POST'])
def GetAllInfos():
    record:[str] = json.loads(request.data)
    if not record or len(record) < 0 and type(record) != list: return "Not"
    NewData = []
    for AssetID in record:
        FlipBook , Size , asseteID = Main(AssetID)
        NewData.append({
            "AssetID":asseteID,
            "FlipBook":FlipBook,
            "Size":Size,
        })
    return jsonify(NewData)


if __name__ == "__main__":
    print("true")
    app.run(debug=True,port=8080,use_reloader=False)


"""
for name in imgDict:
    id = imgDict[name]
    FlipBook , Size , asseteID = Main(id)
    newAssetsData.append({
        "name":name,
        "AssetID":asseteID,
        "FlipBook":FlipBook,
        "Sizes":Size,
    })
dt.Write(newAssetsData , "ToLua65")

LU.Lua(dt.Read("ToLua65") , "MyLulu_Max_65")

file_list = FilesList(r"C:\Users\41794\Downloads\sq")
    file_list.GetList()
    imgList = file_list.GetFiles()

    imgDict = dt.Read("Assets")
    newAssetsData:list[dict] = []
"""
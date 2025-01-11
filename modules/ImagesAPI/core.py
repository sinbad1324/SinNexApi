
from modules.ImagesAPI.PixelImg import Img
from modules.ImagesAPI.Template import Temp
from modules.ImagesAPI.Grid import Ggrid
from modules.ImagesAPI.filtreduplicate import getImages , NoCloneId , GetPreLoadedImg
import gc
def Main(img: tuple):
    # try:
        newimg = Img(img )
        cat = newimg.getCompare()
        id = newimg.OriginaleID
        NewTemp = Temp(newimg)
        GetGrid = Ggrid(NewTemp) 
        GetGrid.GetGridTemplate()
        FlipBook = GetGrid.GetResult() 
        Size = newimg.GetImgSize() 
        GetGrid = None
        NewTemp = None
        newimg = None
        return FlipBook , Size , id, cat
    # except ValueError as e  :
    #     print(e)
    # return False , False, False , None


    # toSave = []
            # toSave.append({
            #     "name": "none",
            #     "AssetID": ids,
            #     "Flipbook": flip,
            #     "Size": {
            #         "x": size["x"],
            #         "y": size["y"]
            #     },
            #     "cat":cat
            # })

def normal(images , JSONdict = {})-> dict:
    for img in images :
        flip , size , id  , cat=  Main(tuple(img))
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
    gc.collect()
    return JSONdict

def GetAll(record , mode = "normal" ,extrem:int = 1 ):
    mode = "normal"
    record =  NoCloneId(record)
    newRecord , JSONdict = GetPreLoadedImg(record)
    images = getImages(newRecord,extrem)
    if mode == "strict":
        JSONdict={}
        for img in images:
            flip , size , id  , cat=  Main(tuple(img))
            if flip and size and id and cat :
                if cat not in JSONdict:
                    if cat.lower() != "beam":
                        JSONdict[cat] ={
                            "Assets":[],
                            "Flipbook":{
                                "Assets":[]
                            },
                            "Textures":{
                                "Assets":[]
                            }
                        }
                        if flip.lower() != "none":
                            JSONdict[cat]["Flipbook"]["Assets"].append({
                                    "name": "none",
                                    "AssetID": id,
                                    "Flipbook": flip,
                                    "Size": {
                                        "x": size["x"],
                                        "y": size["y"]
                                    },
                                "cat":cat 
                                })
                        else:
                                JSONdict[cat]["Textures"]["Assets"].append({
                                    "name": "none",
                                    "AssetID": id,
                                    "Flipbook": flip,
                                    "Size": {
                                        "x": size["x"],
                                        "y": size["y"]
                                    },
                                "cat":cat 
                                })
                    else:
                        JSONdict[cat] ={
                            "Assets":[]
                        }
                        JSONdict[cat]["Assets"].append({
                            "name": "none",
                            "AssetID": id,
                            "Flipbook": flip,
                            "Size": {
                                "x": size["x"],
                                "y": size["y"]
                            },
                        "cat":cat 
                        })
        return JSONdict
    else:
        newRecord = None
        record = None
        mode = None
        return normal(images, JSONdict)





from modules.PixelImg import Img
from modules.Template import Temp
from modules.Grid import Ggrid

def Main(path):
    try:
        newimg = Img(path )
        cat = newimg.getCompare()
        NewTemp = Temp(newimg)
        GetGrid = Ggrid(NewTemp) 
        GetGrid.GetGridTemplate()
        
        FlipBook = GetGrid.GetResult() 
        Size = newimg.GetImgSize() 
        return FlipBook , Size , newimg.OriginaleID , cat
    except :
        return False , False, False , None


def GetAll(record):
    JSONdict={}
    for img in record:
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
                },
            "cat":cat 
            })
    return JSONdict

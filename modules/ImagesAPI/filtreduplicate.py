from modules.ImagesAPI.LoadData import getConvertedImage, model
import modules.ImagesAPI.GetImgSize as hp
import torch
import PIL
import gc
import concurrent.futures
import modules.Json as js
# ConvertedImage =   getConvertedImage(img)

preloadedData = js.Read("JSON/PreloadAssets")

def getCompare(input_features, input_features2, extrem: int) -> bool:
    similarity = 0
    similarity = (input_features @ input_features2.T).mean().item()
    sim = 0.99
    if extrem == 2:
        sim = 0.97
    elif extrem == 3:
        sim = 0.95
    elif extrem == 4:
        sim = 0.925
    elif extrem == 5:
        sim = 0.90
    elif extrem == 0:
        sim = 1
    return similarity >= sim


def NoCloneId(ids):
    return list(set(ids))

def getImages(paths, extrem: int):
    try:
        images = {}
        noDupData = {}
        for i in range(len(paths)):
            img, id = hp.OpenImg(paths[i])
            if img and id:
                img = img.convert("L")
                with torch.no_grad():
                    input_features = model.encode_image(getConvertedImage(img))
                    input_features /= input_features.norm(dim=-1, keepdim=True)
                images["img" + str(i)] = [input_features, img, id]
        for img in images.keys():
            if len(noDupData) >= 1:
                isDouble = False
                for img2 in noDupData.keys():
                    if getCompare(images[img][0], noDupData[img2][0], extrem) == True:
                        isDouble = True
                        break
                if not isDouble:
                    noDupData[img] = images[img]
            else:
                noDupData[img] = images[img]
        images = None
        gc.collect()
        return noDupData.values()
    except PIL.UnidentifiedImageError as e:
        print(e)
    return []


# def getImages(paths, extrem: int):
#     try:
#         images = {}
#         noDupData = {}
#         for i in range(len(paths)):
#             img, id = hp.OpenImg(paths[i])
#             if img and id:
#                 img = img.convert("L")
#                 with torch.no_grad():
#                     input_features = model.encode_image(getConvertedImage(img))
#                     input_features /= input_features.norm(dim=-1, keepdim=True)
#                 images["img" + str(i)] = [input_features, img, id , paths[i]]
#         # for img in images.keys():
#         #     if len(noDupData) >= 1:
#         #         isDouble = False
#         #         for img2 in noDupData.keys():
#         #             if getCompare(images[img][0], noDupData[img2][0], extrem) == True:
#         #                 isDouble = True
#         #                 break
#         #         if not isDouble:
#         #             noDupData[img] = images[img]
#         #     else:
#         #         noDupData[img] = images[img]
#         # images = None
#         # gc.collect()
#         # print(len(noDupData.keys()), "data")
#         return images.values()
#     except PIL.UnidentifiedImageError as e:
#         print(e)
#     return []



def GetPreLoadedImg(path):
    JSONdict = {}
    newpaths = []
    for id in path:
        ins = False
        for data in preloadedData:
            if  id in data["AssetID"]:
                ins = True
                if data["cat"] not in JSONdict:
                    JSONdict[data["cat"]] ={"Assets":[]}
                JSONdict[data["cat"]]["Assets"].append({
                    "name": "none",
                    "AssetID": data["AssetID"][0],
                    "Flipbook": data["Flipbook"],
                    "Size": {
                        "x": data["Size"]["x"],
                        "y": data["Size"]["y"]
                    }
                })
                break
        if not ins:
            newpaths.append(id)
    return newpaths , JSONdict
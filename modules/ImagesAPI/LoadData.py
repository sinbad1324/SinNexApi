import clip 
import os
import pickle

from torchvision import transforms

device =  "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)
# ici le Vi-B/32 -> Vision Transformer 32px sur 32px 

def loadFeaturesFromFile():
    features_file= "Data/pickle/Data"
    if os.path.exists(features_file):
        with open(features_file, 'rb') as f:
            category_features = pickle.load(f)
        return category_features
    return None  

def getConvertedImage(img):
    #Start fait par chatGPT (Copy)
    return preprocess(img).unsqueeze(0).to(device)
    #end fait par chatGPT(copy)




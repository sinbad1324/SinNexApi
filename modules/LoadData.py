import clip
import torch
from PIL import Image
import os
import pickle
import modules.Json as dj

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

data = r"C:\Users\41794\Desktop\Img-categorizations\assets\Data\Cat"

def SetLoadedImages():
    categories = {}
    for path, folder, files in os.walk(data):
        if len(folder)  <= 0 and len(files)  >= 1:
            folder_name = os.path.basename(path)
            if folder_name not in categories:
                categories[folder_name] = []
            for v in files:
                if v.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    categories[folder_name].append(os.path.join(path, v))
    dj.Write( categories,"Generated_images")
    return categories

def getLoadedImages():
    return dj.Read("Generated_images")



def save_features_to_file(category_features , name):
    with open("Data/pickle/"+name, 'wb') as f:
        pickle.dump(category_features, f)

def load_features_from_file(name):
    features_file= "Data/pickle/"+name
    if os.path.exists(features_file):
        with open(features_file, 'rb') as f:
            category_features = pickle.load(f)
        return category_features
    else:
        print("Le fichier des caractéristiques n'existe pas. Encodage des images...")
        return None  # Signale que le fichier doit être créé


def categoris():
    category_features = load_features_from_file("Loaded")
    if category_features is None:
        category_features ={}
        categories = getLoadedImages()
        if categories is None : return {}
        for category, image_paths in categories.items():
            if not image_paths : continue
            images = [preprocess(Image.open(path).convert('RGB')).unsqueeze(0).to(device) for path in image_paths]
            images_tensor = torch.cat(images)

            with torch.no_grad():
                features = model.encode_image(images_tensor)
                features /= features.norm(dim=-1, keepdim=True)
            category_features[category] = features
            save_features_to_file(category_features , "Loaded")
    return category_features


def getConvertedImage(img):
    return preprocess(img.convert('RGB')).unsqueeze(0).to(device)



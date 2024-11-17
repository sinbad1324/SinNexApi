from PIL import Image ,ImageDraw , ImageOps
import numpy as np
import clip  
import torch
from PIL import Image
import matplotlib.pyplot as plt
import modules.GetImgSize as hp
from modules.LoadData import getConvertedImage , loadFeaturesFromFile



device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)


category_features = loadFeaturesFromFile() 


def pixelate(image, pixel_size):
    small_image = image.resize(
        (image.width // pixel_size, image.height // pixel_size),
        resample=Image.BILINEAR
    )
    pixelated_image = small_image.resize(
        (image.width, image.height),
        resample=Image.NEAREST
    )
    return pixelated_image




class Img:
    def __init__(self,path , pxlSize = 10) -> None:

        self.comparedUsed = False
        img ,self.OriginaleID =  hp.OpenImg(path)
        if img == None : return None
        self.ConvertedImage = img
        img = img.convert("RGBA")

      #  gray_image = ImageOps.grayscale(img)
        gray_image = img.convert("L")
        #gray_image.show("gray_image")

        gray_array = np.array(gray_image)

        self.threshold_value = 127
        binary_array = np.where(gray_array >  self.threshold_value, 0, 255).astype(np.uint8)
        self.binary_image = Image.fromarray(binary_array)
        self.pixel_size = pxlSize
        pixelated_image = pixelate(self.binary_image, self.pixel_size)

        img_pixels = np.array(pixelated_image)

        self.img = img
        self.img_pixels = img_pixels

        self.draw = ImageDraw.Draw(img)
        self.candrawDev =False
        self.Raduis = 1

    def GetSize(self , template , div=1 , padd:int=0):
        if self.img == None: return [(0,0),(0,0 , 0  , 0 )]
    #    bbox = self.img.getbbox()
        bbox = self.binary_image.getbbox() 
        if bbox is None:
            bbox = self.img.getbbox()
        x_s,y_s , x_e  , y_e = bbox
    
        x =  int((x_e  - x_s)-padd)
        y =  int((y_e  - y_s)-padd)

        self.Col = int(x/template)
        self.Row = int(y/template)

        if div > 1 :
            x_e = self.Col +x_s
            y_e = self.Row + y_s

            x =  int((x_e  - x_s)-padd)
            y =  int((y_e  - y_s)-padd)

            self.Col = int(x/div)
            self.Row = int(y/div)
        return [(x,y),(x_s,y_s , x_e  , y_e )]

    def GetImgSize(self):
        if self.img == None: return {"x" :0 , "y":0}
        width, height = self.img.size
        return  {"x" :width , "y":height}

    def Line(self , GetCalc:tuple, candraw:bool=False):
        if self.candrawDev == True or candraw:
            self.draw.line(GetCalc, fill='green', width=2)

    def Debug(self ,xy , tec:str ,candraw=False):
        if self.candrawDev == True or candraw:
            if tec == "row":
                self.draw.rounded_rectangle(xy ,50 , fill="blue" , outline="purple" )
            elif tec == "col":
                self.draw.rounded_rectangle(xy ,50 , fill="yellow" , outline="blue" )

    def Show(self , p=False):
        
        if p:
            plt.imshow(self.img_pixels, cmap='gray')
            plt.title('Pixelated Image')
            plt.show()
        else:
            self.img.show()

    def getCompare(self):
        if self.comparedUsed :
            print("Vous avez deja utilisé cette function c'es seulement une fois deso! :[ ") 
            return 
        self.comparedUsed = True
        self.ConvertedImage =   getConvertedImage(self.ConvertedImage)
        # start chatGPT
        similarities = {}
        with torch.no_grad():
            input_features = model.encode_image(self.ConvertedImage)
            input_features /= input_features.norm(dim=-1, keepdim=True) 

        for category, features in category_features.items():
            similarity = (input_features @ features.T).mean().item() 
            similarities[category] = similarity
        # end chatGPT
        predicted_category = max(similarities, key=similarities.get)
        #print(f"La catégorie prédite est : {predicted_category} pour cette img {self.OriginaleID}")
        return predicted_category



"""clr != (0, 0, 0, 0) and
            clr != (0, 0, 0) and
             clr != (0, 0, 0,255) and
            clr != (0, 0, 255, 255) and
            clr != (0, 0, 255) and
            clr != (255, 0, 0, 255) and
            clr != (255, 0, 0) and
            clr != (0,255,0) and
            clr!= (0, 128, 0, 255) and
            clr!= (255, 255, 255, 0) and"""

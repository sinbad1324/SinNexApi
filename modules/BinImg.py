from PIL import Image, ImageOps
import numpy as np

def pixelate(image, pixel_size):
    small_image = image.resize(
        (image.width // pixel_size, image.height // pixel_size),
        resample=Image.NEAREST
    )
    pixelated_image = small_image.resize(
        (image.width, image.height),
        resample=Image.NEAREST
    )
    return pixelated_image

class MyImage:
    def __init__(self,path:str , threshold_value:int = 127) -> any:
        self.img = False
        image = Image.open(path)
        
        gray_image = ImageOps.grayscale(image)
        gray_array = np.array(gray_image)

        self.threshold_value = threshold_value
        binary_array = np.where(gray_array > threshold_value, 0, 255).astype(np.uint8)
        self.image = pixelate(Image.fromarray(binary_array) , 1)

        
    
    def show(self ,NewImg:any = None):
        if NewImg is None:
            NewImg = self.image
        NewImg.show()

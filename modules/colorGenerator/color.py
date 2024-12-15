import random
import math

def clamp(n, min, max): 
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n 

def randomColor():
     return tuple(random.choice(range(255)) for _ in range(3))


def GenerateColor(gradient:bool=False ,points=random.randint(2,16)):
    points = clamp(points ,2,16)
    if gradient:
        seq=[]
        for i in range(points):
            seq.append({
                "time":(random.randint(0,100)/100),
                "color":randomColor(),
            })
        return seq
    else:
        return randomColor()
    


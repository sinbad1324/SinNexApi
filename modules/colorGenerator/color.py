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


def GenerateColor(points=0):
    points = clamp(points,0,18)
    if points >= 2:
        seq=[]
        for i in range(points+1):
            time = (random.randint(0,100)/100)
            if i==0:
                time = 0
            elif i==points:
                time = 1
            seq.append({
                "time":time,
                "color":randomColor(),
            })
        seq.sort(key=lambda x: x["time"],reverse=False)
        return seq
    else:
        color =randomColor()
        
        return [
            {
                "time":0,
                "color":color,
            },
            {
                "time":1,
                "color":color,
            },
        ]
    
# print(GenerateColor(6))
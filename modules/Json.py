import json

def Write(dict:dict| list , file:str)->None:
    Path = f"Data/{file}.json"
    json_object = json.dumps(dict, indent=4)
    with open(Path, "w") as json_file:
        json_file.write(json_object)

def Read(file:str , _type:dict | list={}) -> dict:
    Path = f"Data/{file}.json"
    with open(Path, "r") as json_file:
        if type(_type) == dict:
            return json.load(json_file) or {}
        else:
            return json.load(json_file) or [] 
    

def AddJSON(index =None, value=None ,file:str=None)-> None:
    t = {}
    if index == None:
        t=[]
    data = Read(file , t)
    if type(data)  == dict:
        data[index] = value
    elif type(data) == list:
        data.append(value)
    Write(data, file)
def Lua(table:dict | list , ToSavePath:str):
    LuaText:str = "local module = {\n"
    for i in table:
        dic = i
        size:str = "{\n"
        size += f"  x={dic["Size"]["x"]},\n    y={dic["Size"]["y"]},\n"
        size += "\n}"
        LuaText += "{\n"
        LuaText += f"AssetID = '{dic["AssetID"]}',\n Flipbook = '{dic["Flipbook"]}' ,\n Size = {size}"
        LuaText += "\n},\n"
    LuaText += "\n}"
    with open(f"Lua/{ToSavePath}.lua" , "w") as l:
        l.write(LuaText)
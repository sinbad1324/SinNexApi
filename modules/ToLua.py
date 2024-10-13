def Lua(table:dict | list , ToSavePath:str):
    LuaText:str = "local module = {\n"
    for i in table:
        dic = i
        size:str = "{\n"
        size += f"  x={dic["Sizes"]["x"]},\n    y={dic["Sizes"]["y"]},\n"
        size += "\n}"
        LuaText += "{\n"
        LuaText += f"AssetID = '{dic["AssetID"]}',\n Flipbook = '{dic["FlipBook"]}' ,\n Size = {size}"
        LuaText += "\n},\n"
    LuaText += "\n}"
    with open(f"Lua/{ToSavePath}.lua" , "w") as l:
        l.write(LuaText)
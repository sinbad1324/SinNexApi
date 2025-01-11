class Ggrid:
    def __init__(self , NewTemp ) -> None:
        self.TamplateIS = ""
        self.NewTemp = NewTemp
        self.Dev = False
        self.x4Padd = 0
        self.x2Padd = 0
        self.x8Padd= 0
        
        self.draw = False


        self.X8X = self.NewTemp.Template(8 ,self.x8Padd  ,candraw=self.draw)
        self.X4X  = self.NewTemp.Template(4  ,self.x4Padd  ,candraw=self.draw ) 
        self.X2X  =  self.NewTemp.Template(2 ,self.x2Padd ,candraw=self.draw )
    #    self.X2X_2X = self.NewTemp.Template(4 , self.x2Padd, div=2  ,candraw=self.draw)



    def get8X8Template(self):
        if self.Dev:
            print("==============8X8 Started==================")
        if  self.X8X and  self.X4X and self.X2X  :
            self.TamplateIS = "8X8"
            if self.Dev:
                print("==============8X8 FUNDED==================")
            return "8X8"
        #print("Grid Found \n" , "8X8")
        if self.Dev:
            print("==============8X8 ended==================")
        return False

    def get4X4Template(self):
        if self.Dev:
            print("==============4X4 Started==================")
        if not self.X8X and  self.X4X and self.X2X  : #and not self.X2X_2X
            self.TamplateIS = "4X4"
            if self.Dev:
                print("==============4X4 FUNDED==================")
            return "4X4"
        if self.Dev:
            print("==============4X4 ended==================")
        return False

    def get2X2Template(self):
        if self.Dev:
            print("==============2X2 Started==================")
        if not self.X8X and not self.X4X  and self.X2X :
            self.TamplateIS = "2X2"
            if self.Dev:
                print("==============2X2 FUNDED==================")
            return "2X2"

        #  print("Grid Found \n" , "2X2")
        if self.Dev:
            print("==============2X2 ended==================")
        return False

    def GetGridTemplate(self):
        if self.NewTemp.newimg.GetImgSize()["x"] <= 200:
            self.TamplateIS = "None"
            return "No Grid Found" 
        if  self.get2X2Template() == False:
            if self.get4X4Template() == False:
                if self.get8X8Template() == False:
                    self.TamplateIS = "None"
                    return "No Grid Found"
            
        return f"Grid Found : {self.TamplateIS}"

    def SetDev(self,value):
        self.Dev = value
        self.NewTemp.Dev = value

    def GetResult(self):
        return self.TamplateIS
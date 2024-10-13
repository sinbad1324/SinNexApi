import os


class FilesList():
    def __init__(self , path):
        self.Files = {}
        self.path =  path
    
    def GetList(self , path=None):
        if path is None:
            path = self.path 
        for path , folder , file in os.walk(path):
            if folder :
                for fol in folder:
                    self.GetList(path+"\\"+fol)
            for f in file:
                self.Files[f] = self.path+"\\"+ f
    def GetFiles(self):
        return self.Files        


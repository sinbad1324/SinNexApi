def cond(clr):
    #return (clr != 0 and clr != 75 and clr !=  182 )
    return (clr != 255 and clr < 150)
class Temp:
    def __init__(self ,newimg) -> None:
        
        self.newimg = newimg
        self.img_pixels = newimg.img_pixels
        self.IsTrue ="True\n"
        self.Dev = False
        self.Temp=1
        self.div = 1
        self.padding = 0
        self.candraw = False

    def  Row(self):
            
        NewSize =  self.newimg.GetSize( self.Temp, self.div , self.padding )
        x_s,y_s , x_e  , y_e = NewSize[1]

        for c in range( self.Temp):
            if c <  self.Temp and c > 0:
                
                line =  self.newimg .Col*c + x_s
                self.newimg .Line((line + 1 ,y_s , line + 1, y_e),self.candraw)
                if self.Dev :
                    print("Index C : " ,c , "Line for Row ->(X axe):" , line)
                for i in range(y_s , y_e):
                    try:
                        if line > y_e or i > y_e : return False
                        clr = self.img_pixels[line , i]
                        if  cond(clr):
                            self.IsTrue += f"Fund color in Y {clr}, line {i},{line}\n"
                            self.newimg .Debug((i,line , i+ self.newimg .Raduis , line+ self.newimg .Raduis) , "row" ,self.candraw)
                            return False
                    except IndexError:
                        print("not stop")
                        return False
        return True

    def Column(self):
        
        NewSize =  self.newimg.GetSize( self.Temp , self.div , self.padding )
        x_s,y_s , x_e  , y_e = NewSize[1]

        for c in range( self.Temp):
            if c <  self.Temp and c > 0 :
                line =  self.newimg.Row*c + y_s 
                self.newimg.Line((x_s ,line +1 , x_e,line +1),self.candraw)
                if self.Dev :
                    print("Index C : " ,c , "Line for Colum ->(Y axe):" , line)
                for i in range(x_s , x_e):
                    try:
                        if line > x_e or i > x_e : return False
                        clr = self.img_pixels[i, line]
                        if  cond(clr):
                            self.IsTrue += f"Fund color in X {clr}, line {i},{line}\n"
                            self.newimg.Debug((i,line , i+ self.newimg.Raduis , line+ self.newimg.Raduis) , "col" ,self.candraw)
                            return False
                    except IndexError:
                        return False
        return True
                        

    def Template(self,Template ,padding=0 ,div=1 ,candraw:bool=False):
      
        self.Temp=Template
        self.div = div
        self.padding = padding
        self.candraw = candraw

        row = self.Row()
        col = self.Column()
        if self.Dev:
            print(f"{self.IsTrue}------Tamplate: {Template}x{Template}" , "\n" ,"------Row", row,  "\n" ,"------Col", col)
        self.IsTrue = ""
        return row and col

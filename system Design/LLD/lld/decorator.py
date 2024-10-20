class Color :
    def fill(self) :
        pass
    
#Concrete component of base class 
class Black(Color) :
    def fill(self) :
        print("Black color")
        
#decorator class
class ColorDecorator(Color) :
#base class object
    colored = Color()
#constructor with base class object as the parameter
    def __init__(self, colored) :
        self.colored = colored
    def fill(self) :
        self.colored.fill()
        
#concrete decorator class inheriting base decorator class
class PatternDecorator(ColorDecorator) :
    def fill(self) :
        self.colored.fill()
        self.addPattern(self.colored)
    def addPattern(self, colored) :
        print("Pattern")
        
class Demo :
    @staticmethod
    def main( args) :
        black = Black()
        pattern = PatternDecorator(Black())
        print("\nStyle: Solid")
        black.fill()
        print("\nStyle: Pattern")
        pattern.fill()
    

if __name__=="__main__":
    Demo.main([])

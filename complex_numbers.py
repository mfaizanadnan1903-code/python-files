class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def __add__(self,other):
        return Complex(self.real+other.real , self.img+other.img)
        
    def __sub__(self,other):
        return Complex(self.real-other.real , self.img-other.img)
        
    def show_add(self):
        return f"{self.real} + {self.img}j"
        
    def show_sub(self):
        return f"{self.real} - {self.img}j"
        
c1 = Complex(5,6)
c2 = Complex(2,1)
c3 = c1+c2
print(c3.show_add())

c4 = c1-c2
print(c4.show_s)
from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2
    

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    
obj=Circle(2)
obj2=Rectangle(3,4)

print("area of circle:",obj.area())               
    
print("area of rectangle:",obj2.area())







    
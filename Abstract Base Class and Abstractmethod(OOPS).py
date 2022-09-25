# from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod

class Shape(ABC):               #or   #class Shape(metaclass=ABCmeta)
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=5

    def printarea(self):
        return self.length*self.breadth

class Square(Shape):
    type="Square"
    sides=4
    def __init__(self):
        self.length=10

    def printarea(self):
        return self.length*self.length

rect1=Rectangle()
sqr1=Square()
print(rect1.printarea())
print(sqr1.printarea())




from abc import ABC,abstractmethod

class shape:
    @abstractmethod
    def printrectangle(ABC):
        pass
        # return 0

class rectangle(shape):
    def __init__(self):
       self.length=8
       self.breadth=9

    def printrectangle(self):
        return self.length*self.breadth

rect1=rectangle()
print(rect1.printrectangle())
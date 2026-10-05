from abc import ABC,abstractmethod

class Vehicle(ABC):
     
     @abstractmethod
     def start(self):
          pass

class car(Vehicle):
     
     def start(self):
        print("car started")

c = car()
c.start()


# another exaample

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


c = Circle(5)

print(c.area())
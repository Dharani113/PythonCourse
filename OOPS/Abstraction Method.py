#it dont have defination having only declaration
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("i have walk and run")
class dog(Animal):
    def move(self):
        print("i can bark")
class lion(Animal):
    def move(self):
        print(" i can roar")
class goat(Animal):
    def move(self):
        print("i have 4 legs")
h=human()
h.move()
d=dog()
d.move()
l=lion()
l.move()
g=goat()
g.move()



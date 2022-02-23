# Polymorphism: one thing in many forms.
# 1.Duck Typing:
class computer:
    def cpu(self):
        print("i5")
    def ram(self):
        print("16")
class computer2:
    def cpu(self):
        print("i3")
    def ram(self):
        print("8")

def cpuram(obj):
    obj.cpu()
    obj.ram()

c1=computer()
c2=computer2()
cpuram(c1)
cpuram(c2)














class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
for animal in (cat1, dog1):
    animal.info()
    animal.make_sound()
    # animal.info()
    # animal.make_sound()

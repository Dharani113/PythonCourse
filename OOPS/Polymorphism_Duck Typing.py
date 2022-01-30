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
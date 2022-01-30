class parent:
    def __init__(self):
        print("calling parent as constructor")
    def parentmethod(self):
        print("parent method")

class child(parent):
    def __init__(self):
        print("calling child as constructor")
    def chlildmethod(self):
        print("child method")


# p1=parent()
# p1.parentmethod()

# c=child()
# c.chlildmethod()


class A:
    def __init__(self, n='Rahul'):
        self.name = n


class B(A):
    def __init__(self, roll):
        self.roll = roll
object = B(23)
print (object.name)
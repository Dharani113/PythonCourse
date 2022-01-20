# class computer:
#     def __init__(self, cpu, ram) -> object:
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("config is", self.cpu, self.ram)
#
#
# com1 = computer('i5', 16)
# com2 = computer('i3', 8)
#
# com1.config()
# com2.config()


# ANS:::::
# config is i5 16
# config is i3 8


# class Agriculture:
#
#     def __init__(self, rabi, karif):
#         self.rabi = rabi
#         self.karif = karif
#
#     def seasons(self):
#         print("seasons of agriculture start from", self.rabi, self.karif)
#
#
# rab = Agriculture('november','1')
# kari = Agriculture('june','2')
#
# rab.seasons()
# kari.seasons()


#EXAMPLE.3//
# class computer:
#     pass
#
# c1=computer()
# print(id(c1))


#52.TYPES OF VARIABLES::
# CLASS VARIABLES AND INSTANCE VARIABLES.
class car:
    wheels=4     #(class variables and class namespace)

    def __init__(self):
        self.company="tata"  #------------->(INSTANCE VARIABLES AND INSTANCE NAMESPACE)
        self.mil=10  #------------->(INSTANCE VARIABLES AND INSTANCE NAMESPACE)
c1=car()
c2=car()
c1.mil=8
c2.company="bmw"

print(c1.company,c1.mil,c1.wheels)
print(c2.company,c2.mil,c2.wheels)

##ANS:
# tata 8 4
# bmw 10 4







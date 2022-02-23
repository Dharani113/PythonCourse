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


# EXAMPLE.3//
# class computer:
#     pass
#
# c1=computer()
# print(id(c1))


# 52.TYPES OF VARIABLES::
# CLASS VARIABLES AND INSTANCE VARIABLES.
# class car:
#     wheels = 4  # (class variables and class namespace)
#
#     def __init__(self):
#         self.company = "tata"  # ------------->(INSTANCE VARIABLES AND INSTANCE NAMESPACE)
#         self.mil = 10  # ------------->(INSTANCE VARIABLES AND INSTANCE NAMESPACE)
#
#
# c1 = car()
# c2 = car()
# c1.mil = 8
# c2.company = "bmw"
#
# print(c1.company, c1.mil, c1.wheels)
# print(c2.company, c2.mil, c2.wheels)


##ANS:
# tata 8 4
# bmw 10 4

# 53.TYPES OF METHODS OF PYTHON::
# 1.INSTANCE METHODS
# 2.CLASS METHODS
# 3.STSTIC METHODS

# class student:
#     student="svist"
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#
#     def avg(self):
#         return(self.m1+self.m2+self.m3)
#     @classmethod
#     def getSchool(cls):
#         return cls.student
#
#
# s1=student(23,34,54)
# s2=student(14,56,76)
# print(s1.avg())
# print(student.getSchool())


# EXAMPLE::
# class patient:
#     name = "basavatarakam"
#
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
#
#     def deases(self):
#         # print("suffering from:",self.p1,self.p2)
#         return ("suffering from:", self.p1, self.p2)
#
#     @classmethod
#     def gethospital(cls):
#         return (cls.name)
#
#
# p1 = patient("cancer,", "heart")
# p2 = patient("cancer,", "brain")
# print(p2.deases())
# print(patient.gethospital())
#
#
#
#
#
#
#
#
#
#
#
#
#



class person:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def person(age):
         print("my age is:" ,age.name)


p1 = person("dha", "white")
p2 = person("sri", "white")

print(p1.name)
print(p2.name)
















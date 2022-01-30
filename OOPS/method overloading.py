# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#
#     def sum(self,a=None,b=None,c=None):
#         s=0
#         if (a!=None,b!=None,c!=None):
#              s=a+b+c
#         elif (a!=None,b!=None):
#              s=a+b
#         else:
#              s=a
#         return s
# s1=student(58,69)
# print(s1.sum(2,2,3))

#METHOD OVERRIDING::
#TWO CLASSES WITH ONE PARAMETER.
class parent:
    def bike(self):
        print("i have suzuki bike")
class child(parent):
    def bike(self):
        print("i have fz 500cc bike")

# ob1=parent()
# ob1.bike()
ob1=child()
ob1.bike()

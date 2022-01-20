# # SYNTAX::
# #WITHOUT PARAMETERS::
# def test():
#     print("TRILOCHAN DHARANI REDDY")
#
# test()

# #WITH PARAMETERS::
# def name(a):
#     print(a-13)
#
# name(15)

# #optinal/default parameters::
# def getcountryname(name="india"):
#     print(name)
# getcountryname()
# getcountryname("usa")
# getcountryname(1000)
#
# #pass list in function::
# def courses(list):
#     for x in list:
#         print(x)
# list1=["java","c","kaak","dkfgdsj"]
# courses(list1)

# def names(set):
#     for x in set:
#         print(x)
# set1={51,8,5,7,8,25,5,7}
# names(set1)

##function with return::
# def add(a,b):
#     c=a+b
#     print(c)#50
#     return c
#
# c=add(30,20)
# print(c)#50
def multiply(a,b,d):
    c=a*b*d
    print(c)
    return
c=multiply(2,3,5)


# def getcapitalname(countryname):
#     if countryname=="india":
#         return "new delhi"
#     else:
#         print("wrong")
# print(getcapitalname("india"))

# def launchbrowser(browsername):
#     if browsername=="chrome":
#         print("launchbrowser is chrome")
#     elif browsername=="firefox":
#         print("launchbrowser is firefox")
#     else:
#         print("none")
#
# launchbrowser("khgjfhj")

# def fact(num):
#     if num>1:
#         num=num*fact(num-1)
#     return num
# print(fact(4))
# print(fact(5))

# def multiple(num):
#         for i in range(1,11):
#             q=num*i
#             print(q)
#
#
# multiple(5)


# def launch(name,age):
#     print("Login in the name of %s  and age is %d" %(age,age))
#
# launch("naveen",25)


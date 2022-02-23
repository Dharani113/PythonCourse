# a map is a  function  executes a specied function for each item in an iterable.
# This item is sent to the function as a (parameter)
# 1.example::
# Make new fruits by sending two iterable objects into the function???????
# def function(a,b):
#     return a+b
# x=map(function,("apple","banana","orange"),("fruit","custurd apple","pinaple"))
# print(x)
# print(list(x))
# #                                    (OR)
# a=("apple","banana","orange")
# b=("fruit","custurd apple","pinaple")
# result=map(lambda a,b:a+b,a,b)
# print(list(result))
#
#
#
# #2.Example::
# # Return double of n????
# def addition(n):
#     return n+n
# numbers=(1,2,3,4,5,6)
# result=map(addition,numbers)
# print(list(result))
#                     #(OR)
# a=(1,2,3,4,5,6)
# result=map(lambda x:x+x,a)
# print(list(result))
#
#
# #3.example:
# # List of strings????
# l=["sat","thu","fri","wed"]
# result=list(map(list,l))
# print(result)

l=[1,2,3,4,5]
# def square(x):
#     return x*x
# b=list(map(square,l))
# print(b)
b=list(map(lambda x:x*x,l))
print(b)
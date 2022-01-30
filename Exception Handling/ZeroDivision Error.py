# Program to handle multiple errors with one
# except statement
# Python 3

# def fun(a):
#     if a < 4:
#         # throws ZeroDivisionError for a = 3
#         b = a / (a - 3)
#
#     # throws NameError if a >= 4
#     print("Value of b = ", b)
#
#
# try:
#     #fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("Zero ")
# except NameError:
#     print("Name")
# # fun(5)



# try:
#     a=5//0
#     print(k)
# except ZeroDivisionError:
#     print("can't divide")
# finally:
#     print("can be divide")

try:
   raise NameError ("hi dharani")

except NameError:
    print("An Error Occured")




# # Program to depict else clause with try-except
# # Python 3
# # Function which returns a/b
# def AbyB(a, b):
#     try:
#         c = ((a + b) / (a - b))
#     except ZeroDivisionError:
#         print("a/b result in 0")
#     else:
#         print(c)
#
#
# # Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)



try:
    a=5
    b=0
    print (a%b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print ('Division by zero not allowed')
print ('Out of try except blocks')
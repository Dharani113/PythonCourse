# x=int(input("please enter the value of x"))
# if x>0:
#     print("x is positive number")
# elif x<0:
#     print("x is negative number")
# elif x==0:
#     print("x is equal to zero")
# else:
#     print("not defined")
#
# if True:
#     print("pass")
# else:
#     print("fail")


# a=10
# b=1000
# c=9000
# if a>b and a>c:
#     print("a is the highest number")
# elif b>c and b>a:
#     print("b is the highest number")
# else:
#     print("c is the highest number")

total = int(input("enter the total value"))
if (total < 100):
    total = total + 50
elif (total >= 100 and total <= 500):
    total = total + 10
else:
    total = total + 25

print(total) ##no concatination method
print("total="+str(total))  ##string method
print(f'{"total value="}{total}') ##f' string method

#FOR 3 DIGITS ONLY:

num = int(input("enter a number"))
sum = 0
temp = num
while (temp > 0):
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is a armstrong number")
else:
    print("not armstromg number")



#for n digits::
# num = int(input("enter a number"))
# order=len(str(num))
# sum = 0
# temp = num
# while (temp > 0):
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if num == sum:
#     print(num, "is a armstrong number")
# else:
#     print("not armstromg number")


# num = int(input("enter a number"))
# order = len(str(num))
# for num in range(0,1000):
#     sum = 0
#     temp = num
#     while (temp > 0):
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#         if num == sum:
#             print(num, "is a armstrong number")
#         break
#     else:
#         print("not armstromg number")


# for num in range(0, 1000):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#         if num == sum:
#             print(num)
# for num in range(100,1000):
#   temp=num
#   sum=0
#   while temp>0:
#       digit=temp%10
#       sum=sum+digit**3
#       temp=temp//10
#       if sum==num:
#            print (num)






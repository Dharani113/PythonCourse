
for num in range(1,25):
    for i in range(2,num//2):
        if num%i == 0:

            break
    else:
        print("Prime number", num)


# #Even
# for i in range(1,101):
#     if i%2 ==0:
#         print("Even Number",i)


# lower = 1
# upper = 25
#
# print("Prime numbers between", lower, "and", upper, "are:")
#
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
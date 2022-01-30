# 1.while::
# count = 0
# # while (count==0):
# #     print("dharani reddy")
# #     count = count + 1
#
# num=0
# while (num<3):
#     print("dharani reddy")
#     num=num+1
# else:
#     print("trilochan reddy")

#
# for i in range(1,5):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# ans:::
# 1
# 2 2
# 3 3 3
# 4 4 4 4


# for i in range(1, 6):
#     for j in range(1,i+1):
#             print(j, end=' ')
#     print()
#ans:::
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5




#     1
#    12
#   123
#  1234
# 12345

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1,i+1):
#             print("*", end=' ')
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1, 6):
#     for j in range(1,6):
#             print(j, end=' ')
#     print()

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
#Program:
size=5
for i in range(size):
    for j in range(1,size-i):
        print(" ",end="")
    for k in range(1,i+2):
        print(k, end='')

#Output:
#     1
#    12
#   123
#  1234
# 12345
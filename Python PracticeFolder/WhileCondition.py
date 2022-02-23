# count=0
# while (count<9):
#     print(count)
#     count=count+1
# print("bye")

# var = 0
# while (var < 9):
#     num = input("enter a number")
#     print("num")
#     var=var+1
# print("bye")


count = 0
while (count < 9):
    print("count:", count)
    count = count + 1
else:
    print("not num")

# FOR::
# 1.
for letters in 'python':
    print(letters)
for numbers in '7036560930':
    print(numbers)

# 2.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(6):
#
#     for j in range(1,i+1):
#         print(j,end=" ")
#
# #     print()
#
# for num in range(10, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i
#             break
#     else:
#         print("prime number,num")


# for num in range(1,20):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print("prime number",num)


count = 3
# while(count<5):
#     print("count")
#     count=count+1
#     if count==1:
#      break
# else:
#      print("not possible")


# for letters in "python":
#     if letters=="x":
#         break
#     print(letters)
# else:
#     print("continue")

name = ["a", "b", "c", "d"]
for i in name:

    if i == "c":
        continue
    print(i)
else:
    print("break")




fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


for x in range(2,30,3):
  print(x)


# for x :
#     print(x)

l1=[10,20,10,30,10]
for i in l1:
   if i>10:
       print("num:",i)

l1=[10,20,10,30,10]
l2=set(l1)
print(l2)

# l1=[10,20,40,50]
# l2=[10,20,30,60,70]
# print(diff(l1,l2))


l1=[10,20,30,40,50]
temp=10
l1[0]=l1[1]
l1[1]=temp
print(l1)


# t1=("dha","drrr",3,4)
# del(t1[0])
# print(t1)

# l1=[10,20,30,40,50]
# print(list.reverse())
# # print(list)

s1=["a","b"]

s2=s1.reverse()
print(s2)

# s1.remove("a")
# print(s1)


s1=["a","b","c"]
s1.reverse()
print(s1)





















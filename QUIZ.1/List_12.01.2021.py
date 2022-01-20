# LIST::
# 1.ANS
# list1 = [1, 2, 3, 5, 4, 8, 7, 9]
# temp_l1 = list1.copy()
# # temp_l1=list1[:]
# list1.sort()
# print(list1)
# print(temp_l1)
#
# # if test expression:
# #     statement(s)
#
# # if
# # if-else
# # elif
#
# if temp_l1 == list1:
#     print("Equal")
# else:
#     print("unEqual")

# 2.ANS::
# list2 = [1, 2, 3, 5, 4, 8, 7, 9]
# for i in list2:
#     if i % 2 == 0:
#         print("Even :", i, end=", ")
#     else:
#         print("Odd :", i, end=",  ")


# l1=[1,2,3,4,90,89]
# #
# # for i in l1:
# #     print("Before if ",i)
# #     if i==90:
# #         break
# #     print("After if ",i)
#
# for i in range(len(l1)):
#
#     if l1[i]==4:
#         break
#     print(l1[i])

#3.ANS::
# l1=[1,2,3,4,90,89]
# l2=[6,7,8,9,10,11]
# l3=l1+l2
# print(l3)
#
# list3 = [1, 2, 4, 6]
# list4 = [9, 3, 19, 7]
# list5 = list3+list4
# print(list5)
# list3.extend(list4)
# print(list3)              #ans:[1, 2, 4, 6, 9, 3, 19, 7]

#4.ans::
# list3 = [1, 2, 4, 6]
# list3[0],list3[-1]=list3[-1],list3[0]
# print(list3)

#5.ANS::
#Program to Subtract a List from Another List
list3 = [1, 2, 4, 6]
list4 = [9, 3, 4, 6]
list5 = []
for i in list3:
    if not i in list4:
        list5.append(i)
print(list5)

list5 = [1, 2, 5, 8]
list6 = [9, 3, 4, 6]
list7 = []
for i in list5:
    if not i in list6:
        list7.append(i)
print(list7)












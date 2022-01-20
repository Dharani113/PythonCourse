# # my_set = {1,2,3,4,5,6,12,24}
# # n = int(input("Enter the number you want to remove"))
# #
# # my_set.discard(n)
# # print("After Removing:",my_set)
# #set()::
# # set1 = {23,44,56,67,90,45,"Javatpoint"}
# # print(set1)
# set1 = {23,44,56,(90,45),("java",45)}
# print(set1)
#
# #set operations::
# #union::
p1 = {23,44,56,67,90,45,"Javatpoint"}
p2 = {24,44,56,67,90,45,"Javatpoint"}
print(p1.union(p2))
#
# #intersection::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# p2 = {24,44,56,67,90,45,"Javatpoint"}
# print(p1.intersection(p2))
#
# #difference of sets::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# p2 = {24,44,56,67,90,45,"Javatpoint"}
# print(p1-p2)
# print(p2-p1)
#
# #symmetric difference::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# p2 = {24,44,56,67,90,45,"Javatpoint"}
# print(p1.symmetric_difference(p2))
# print(p2.symmetric_difference(p1))
#
# #built-in fumctions::
# #adding::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# p1.add("basic")
# print(p1)
#
# #update::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# p1.update(["basic",0])
# print(p1)
#
# #clear::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# p1.clear()
# print(p1)
#
# #copy::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# p2=p1.copy()
# print(p2)
#
# #discard::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# print(p1.discard(23))
# print(p1)
#
# #remove::
# p1 = {23,44,56,67,90,45,"Javatpoint"}
# print(p1.remove(23))
# print(p1)

p1 = {23,44,56,67,90,45,"Javatpoint"}
p2 = {22,45,57,68,91,45,"Javatpoint"}









#adding::
# set1 = {23,44,56,67,90,45,"Javatpoint"}
# set2 = {13,23,56,76,"Sachin"}
# set3=set1.add(set2)
# print("set3")
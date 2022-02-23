# 1.second smallest program:
#
# inputList = int(input("Length of list"))
# list1 = []
# for i in range(inputList):
#     element = int(input("Enter the element"))
#     list1.append(element)
#
# print("List Elements are:", list1)
#
# first_smallest = list1[0]
# second_smallest = list1[1]
# for i in range(len(list1)):
#     if list1[i] < first_smallest:
#         second_smallest = first_smallest
#         first_smallest = list1[i]
#     elif second_smallest > list1[i] != first_smallest:
#         second_smallest = list1[i]
#
# print(second_smallest)




n = [1, 3, 5, 70, 78, 45, 9, 0]
first_largest=n[0]
second_largest=n[1]
third_largest=n[2]
for i in range(2,len(n)):
    if n[i]>second_largest:
        second_largest=first_largest
        third_largest=second_largest
        third_largest=n[i]
    elif n[i]>third_largest and second_largest !=n[i]:
        third_largest=n[i]
print(third_largest)




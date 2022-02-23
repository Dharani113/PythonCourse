inputlist = int(input("length of list"))
list1 = []
for i in range(inputlist):
    element = int(input("enter the element"))
    list1.append(element)
print("elements in a list:", list1)
first_largest = list1[0]
second_largest = list1[1]
third_largest = list1[2]
for i in range(len(list1)):
    if list1[i] > first_largest:
        third_largest = second_largest
        second_largest = first_largest
        first_largest = list1[i]
    elif second_largest < list1[i] != first_largest:

        third_largest = list1[i]

print(third_largest)

# z = list(map(int, input().split()))  # Input list from the user
# max1, max2, max3 = 0, 0, 0  # Initializing max1,max2,max3
# for i in z:  # Iterations
#     if i > max1:  # Comparison for max1
#         max3 = max2
#         max2 = max1
#         max1 = i
#     elif i > max2:  # comparison for max2
#         max3 = max2
#         max2 = i
#     elif i > max3:  # Comparison for max3
#         max3 = i
# print("The Third maximum element in the list is %d" % max3)  # Displays Third largest element in the list

# z = list(map(int, input().split()))  # Input list from the user
# max1, max2 = 0, 0 # Initializing max1,max2,max3
# for i in z:  # Iterations
#     if i > max1:  # Comparison for max1
#         max2 = max1
#         max1 = i
#     elif i > max2:  # comparison for max2
#         max3 = max2
#         max2 = i
#     elif i > max3:  # Comparison for max3
#         max3 = i
# print("The Third maximum element in the list is %d" % max3)  # Displays Third largest element in the list



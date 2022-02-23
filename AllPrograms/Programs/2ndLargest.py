inputList = int(input("Length of list"))
list1 = []
for i in range(inputList):
    element = int(input("Enter the element"))
    list1.append(element)

print("List Elements are:", list1)

first_largest = list1[0]
second_largest = list1[1]


for i in range(len(list1)):
    if list1[i] > first_largest:
        second_largest = first_largest
        first_largest = list1[i]
    elif second_largest < list1[i] != first_largest:
        second_largest = list1[i]

print(second_largest)



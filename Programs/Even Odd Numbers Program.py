# even=0
# odd=0
# for i in range(1,10):
#     if (i%2==0):
#         even+=1
#     else:
#         odd+=1
# print("odd numbers",odd)
# print("even numbers",even)

numbers=(1,2,3,4,5,6,7,8,9)
count_even=0
count_odd=0
for x in numbers:
    if x%2==0:
        count_even+=1
    else:
        count_odd+=1
print("number of even numbers:",count_even)
print("number of odd numbers:",count_odd)
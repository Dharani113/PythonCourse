# num = int(input("enter a value"))
# for i in range(2, num//2):
#     if num % i == 0:
#         print("not a prime number:",num)
#         break
# else:
#     print("prime number",num)

for num in range(2,25):
    for i in range(2, num):
        if num % i == 0:
            print("not a prime number:",num)
            break
    else:
        print("prime number",num)
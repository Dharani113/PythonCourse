# name="dhatri reddy"
# for i in name:
#     print(i)
#     if (i=="x"):
#         break
#     else:
#         continue

###by using range method::
# lan=["c","c++","java","dharu","kesava","tri"]
# for l in range(len(lan)):
#     print(lan[l])
#     if (lan[l]=="kesava"):
#         print("i love kesava")
#         break
#     else:
#         continue


# 2.EXAMPLE::
# lang=["c","c++","java","dharu","kesava","tri"]
# for index in range(len(lang)):
#     print(lang[index])
#     if (lang[index]=="dharu"):
#         print("i love dharu")
#         break
#     else:
#         continue


####Quiz::::
# a=above 80,
# b=60 to 80,
# c=50 to 60,
# d=45 to 50,
# e=25 to 45,
# f=Below 25.
x = int(input("enter the value of x"))
if x > 80:
    print("a")
elif 60 <= x <= 80:
    print("b")
elif 50 <= x <= 60:
    print("c")
elif 45 <= x <= 50:
    print("d")
elif 25 <= x <= 45:
    print("e")
else:
    print("f")

# def name(i):
#     print(i)
#
#
# name("dharani")
#
#
# def function(fname):
#     print(fname + "reference")
#
#
# function("sri")
#
# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Emil", "Tobias", "Linus")
#
#
#
# def names(*args):
#     print("names:",args[2])
# names("dha","sri","drrr","tri","rrrr")
#
#
# def names(**child3):
#     print("names:",child3)
# names(child1="dha",child2="tri",child3="dhdhd")
#
# def sri(**names):
# #     print("differnet names:" +names["name2"])
# # sri(name1="dha",name2="dhaa",name3="dharani")
# #
# #
# # def hospitalnames(**hsn):
# #     for i in hospitalnames():
# #         print("hospita")
# #
# #
l1 = [1, 2, 7, 10, 5, 6]
l1.sort(reverse=True)
print(l1)
#
# l1=[50,65,23,82,100]
# def funt(n):
#     return abs(n-50)
# l1.sort(key=funt)
# print(l1)4

d1 = {"name": "sri", "class": 8}
d3 = {"edcu": 10}
d2 = d1.update(d3)
print(d1)

s1 = {1, 2, 3, "a", "b", "c"}
s2 = [67, 67]
s2.remove(67)
print(s2)

count = 0
while (count == 2):
    num = input("enter num")
    print("num")
    count = count + 1
else:
    print("ok")


def hospitals(names="india"):
    print("diff hospital names:", names)


hospitals("sweden")
hospitals()


def function(food):
    for x in food:
        print(x)
fruits = ["orange", "red", "yellow"]
function(fruits)

def function(x):
    return 5 * x
print(function(3))
print(function(2))




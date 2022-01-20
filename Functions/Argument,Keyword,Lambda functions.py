# # KEY,VALUE pass in a function::
# def login(username, password):
#     print(username, password)
#
#
# login("dharani reddy", "test123@")
#
# login(username="dharanirret", password="test123@")
#
#
# # *arg::
def getmarks(*arg):
    for i in arg:
        print(i)
    return

getmarks(144, 12, 34, 5, 4, 65, 76, 89)
#
#
# ##keyword arg(**args):::
# # represented in **args
# def hospitalnames(**args):
#     for hospital, names in args.items():
#         print("%s == %s" % (hospital, names))
#
#
# hospitalnames(hospital="cancer", name="basavatarakam")
#
# ##lamba function::
# # also called as annonymus function.
# # defination:: a function with out names is called lamba function.
# # example::
#
#
# total = lambda marks: marks + 30
# print(total(100))
#
# square = lambda x: x * x
# print(square(2))
#
# add = lambda x, y, z: x + y + z
# print(add(2,3,5))


# tables = [lambda x=x: x*2 for x in range(1, 11)]
# print(tables())
# # for table in tables:
# #     print(table())




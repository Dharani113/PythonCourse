
# #defenation::
# Each key is separated from its value by a colon (:), the items are separated by commas,
# and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with
# just two curly braces, like this: {}.

#Accessing Values in Dictionary::
# dict1={"name":"dharani","age":22,"class":4}
# print("dict1[name]:",dict1["name"])         #ANS::dict1[name]: dharani
# print("dict1(class):",dict1["class"])       #ans:dict1(class): 4


#Updating Dictionary::
# dict1={"name":"dharani","age":22,"class":4}
# dict1["name"]="tri"
# dict1["age"]=25
# print(dict1)                  #ans:{'name': 'tri', 'age': 25, 'class': 4}
# print(len(dict1))             #ans:3

#Delete Dictionary Elements::
# dict1={"name":"dharani","age":22,"class":4}
# del dict1["name"]
# print(dict1.clear())
# print(dict1)

#Properties of Dictionary Keys::
# (a) More than one entry per key not allowed. Which means no duplicate key is allowed.
# When duplicate keys encountered during assignment, the last assignment wins.
# dict4 = {'Name': 'dha', 'Age': 22, 'Name': 'tri'}
# print("dict4[Name]: ", dict4['Name'])             #ans:dict4[Name]:  tri

#(b) Keys must be immutable. Which means you can use strings,
# numbers or tuples as dictionary keys but something like ['key'] is not allowed.

















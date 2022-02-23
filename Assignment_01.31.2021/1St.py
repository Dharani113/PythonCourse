list1=[1,2,3,"dhatri",35.89]
print(list1)
list1[1]=5
print(list1)
print(list1[3:])
print(list1[0:2])
print("--------------------------------------")
tuple1=(1,2,3,"dhatri",35.89)
print(tuple1)
# tuple1[1]=4        TypeError: 'tuple' object does not support item assignment
# print(tuple1)
print(tuple1[1:4])
print(tuple1[3:])
print("--------------------------------------")

set1={1,2,3,"dhatri",456.66}
print(set1)
# print(set1[1:])  #'set' object is not subscriptable
# set1[1]=2        #'set' object does not support item assignment
# print(set1)
print("--------------------------------------")

dict1={"name":"dharani","class":"inter"}
print(dict1)
dict1["name"]="tri"
print(dict1)
print(dict1.keys())
print(dict1.values())
print("--------------------------------------")
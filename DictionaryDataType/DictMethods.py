 # 1.Python dictionary clear() Method::
dict1={"name":"dharani","age":22,"class":4}
print("start len:",len(dict1))
dict1.clear()
print("end len:",len(dict1))
print(dict1)

 #2.Python dictionary copy() Method::
dict1={"name":"dharani","age":22,"class":4}
dict2=dict1.copy()
print(dict2)

#3.Python dictionary fromkeys() Method
 # seq=("name","age","class")
 # dict=dict.fromkeys(seq)
 # print("new dict:",dict)
 # dict2=dict2.fromkeys(seq,10)

#4 GET METHOD::
dict1={"name":"dharani","age":22,"class":4}
print("value:",dict1.get("age"))

#5.Python dictionary items() Method::
dict1={"name":"dharani","age":22,"class":4}
print("items:",dict1.items())

#6.Python dictionary keys() Method::
dict1={"name":"dharani","age":22,"class":4}
print("keys:",dict1.keys())

#7.Python dictionary values() Method::
dict1={"name":"dharani","age":22,"class":4}
print("values:",dict1.values())

#8.Python dictionary setdefault() Method::
dict1={"name":"dharani","age":22,"class":4}
print("value:",dict1.setdefault("age","none"))
print("value:",dict1.setdefault("class","none"))
# print("value:",dict1.setdefault("sex","none"))

#9.Python dictionary update() Method::
dict1={"name":"dharani","age":22,"class":4}
dict2={"sex":"female"}
dict1.update(dict2)
print("value:",(dict1))

#10.














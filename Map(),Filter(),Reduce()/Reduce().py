import functools
list=[1,2,3,4,5,6,7,8,19,0]
print(functools.reduce(lambda a,b:a+b,list))
print(functools.reduce(lambda a,b:a-b,list))
print(functools.reduce(lambda a,b:a if a<b else b,list))
print(functools.reduce(lambda a,b:a if a>b else b,list))
var1 = ' hello World! '
var2 = 'hello\tWorld!'
var3 = 'helloWorld1233'
print(var1)
print(var1[0])
print(var1[3:])
print(var1[:3:])
print(var1[3:10])
print("Update String : ",var1[:6]+'Python')
print(len(var1))
print(var1.capitalize())
print(var1.center(16,'T'))
print(var1.count('h',0,len(var1)))
print(var1.endswith('d!',10,12))
print(var2.expandtabs())
print(var2.expandtabs(16))
print(var1.find("World",0,len(var1)))
print(var1.index('l',5,len(var1)))
print(var1.isalnum())
print(var3.isalnum())
print(var1.isalpha())
print(var3.isnumeric())
print(var3.isdigit())
print(var1.islower())
print(var1.isspace())
print(var1.istitle())
print(var1.isupper())
s1='-'
seq="a","b"
print(s1.join(seq))
print(var1.ljust(20,'0'))
print(var1.lstrip())
name="trilochAn is gud boy"
print(name.count('o'))
print(name.find('o',5))
count=0
for i in name:

    if i=='o':
        count=count+1
        print(i)
print(count)


#REPLACE:
print(name.replace('gud','bad'))
print(max(name))
#SPLIT:
print(name.split('i'))
#REVERSE:
var2='hello world'[::-3]
print(var2)
print(name.startswith('t'))
print(name.endswith('y'))
print(name.endswith('x'))
print("trilochan is gud{}".format(' boy'))
print(name.upper())
print(name.capitalize())
print(name.title())
#join:
s1="trilochan"
s2='-'
print(s2.join(s1))


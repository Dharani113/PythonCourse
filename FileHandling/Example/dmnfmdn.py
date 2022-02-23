import os
#SEEKING::
school=open("school names.txt","w+")
names=["dharani","trilochan","sree","kesava reddy"]
school.write("all students names")
for i in names:
    school.writelines(i)
    print()
# print(school.read(names))
school.seek(0)
l=os.path.getsize("school names.txt")
print(l)
print(school.read(l))


# #APPEND::::
# school=open("school names.txt","w+")
# names=["dharani\n","trilochan\n","sree\n","kesava reddy\n"]
# school.write("all students names\n")
# school.writelines(names)
# print(school.read())
# school=open("school names.txt","a")
# school.write("maheswari\n")
# school=open("school names.txt","r")
# print(school.read())



# Accesing List:
list1=["dharani",10,"tri",234.546,10]
print("list1[0]:",list1[0])
print("list1[1]:",list1[1])
print("list1[1:3]:",list1[1:3])
print("list1[1:4]:",list1[1:4])

#updating list
print("list1[1]:",list1[1])
list1[1]=24
print("list1[1]:",list1[1])
list1[3]="chadulla"
print("list1[3]:",list1[3])

#Delete List Elements
del list1[1]
print("list1:",list1)
del list1[3]
print("list1:",list1) #ans:list1: ['dharani', 'tri', 'chadulla', 10]

#Basic List Operations
#length:
print(len(list1)) #ans:3

#concatination:
print(list1+[4])
print(list1+[4]+[5]+[7])

#repetition:
print(list1*2)  #ANS:['dharani', 'tri', 'chadulla', 'dharani', 'tri', 'chadulla']

#MEMBERSHIP:
print(2 in list1)  #ans:False
print("dharani" in list1)    #ans:True

#iteration:
 #aftr loops we can exicute
#INDEXING,SLICING,MATRIXES:
list2=[123,"kesava",208.456,"spam%"]
print(list2[1])    #ANS:kesava
print(list2[0:])   #ANS:[123, 'kesava', 208.456, 'spam%']
print(list2[-2])   #ans:208.456(how we will count from -1 to or from 0)
print(list2[-3])   #ans:kesava
print(list2[1:3])






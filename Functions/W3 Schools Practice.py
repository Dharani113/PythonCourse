# Arbitrary Arguments::(*arg)
def my_function(*kids):
    print("The youngest child is ", kids[2])


my_function("Emil", "Tobias", "Linus")
print("---------------------------------------------------")


# Keyword Arguments::
def my_function(kid1, kid2, kid3, kid4):
    print("The youngest child is ", kid4)


my_function("kid1=Emil", "kid2=Tobias", "kid3=Linus", "kid4=toshoiba")
print("---------------------------------------------------")


# Arbitrary Keyword Arguments, **kwargs::
def my_function(**sri):
    print("hospial name is " + sri["name2"])


my_function(name1="basava", name2="taarak")


# Default Parameter Value:
def family(name="dharani"):
    print("my name is " + name)


family("sree")
family()
family("kesava")


def name(a):
    print(a - 13)


name(18)

#using return statement:
def name(a):
    return (a - 13)


name(18)

#The Pass Statement:
name="dharanxi"
for i in name:
  if(i=="x"):
    continue
  else:
    pass
  print(i)
# OUTPUT: dharan


name="dharanxi"
for i in name:
  if(i=="x"):
    continue
  else:
    break
  print(i)
# OUTPUT:NOTHING WILL COME



try:
    x=int(input("enter a value"))
    if x>2:
        raise ValueError(x)
except Exception as e:
    print(e)
    print("x is out of range")
else:
    print("x value is in range")
finally:
    print("ok")


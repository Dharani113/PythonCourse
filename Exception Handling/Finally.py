a = 0
try:
    if a < -1:
        print("A is Greater")
    else:
        pass
    try:
        if a<=-1:
              print("A is Greaterthan")
        else:
            pass
    finally:
        print("Hello")
except UserWarning:
    print("A is undefined")
class A:
    def __init__(self):
        print("A is working")
    def feature1 (self):
        print("feature 1 is working")
    def feature2 (self):
        print("feature 2 is working")
class B:
    def __init__(self):
        print("B is working")

    def feature3 (self):
        print("feature 3 is working")

    def feature4 (self):
        print("feature 4 is working")
class C(A,B):
    def __init__(self):
        super(). __init__()
        print("C is working")
a1=C()







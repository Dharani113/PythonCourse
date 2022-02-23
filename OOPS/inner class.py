class student:
    student="svist"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.lap=self.laptap()

    def show(self):
        print((self.m1+self.m2+self.m3)/3)
        self.lap.show()
        # return(self.m1+self.m2+self.m3)/3


class laptap:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram="16"

        def show(self):
            print(self.brand,self.ram,self.cpu)

s1=student(23,34,54)
#s2=student(14,56,76)
s1.show()


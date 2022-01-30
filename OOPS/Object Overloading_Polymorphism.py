class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other1):
        m1 = self.m1 + other1.m1
        m2 = self.m2 + other1.m2
        s4=student(m1,m2)
        return s4
    def __add__(self, s2):
        s1=self.m1+self.m2
        total=student(s1)
        return total

s1 = student(23, 32)
s2 = student(34, 43)
s4 = s1 + s2
print(s4.m2)
print(total.s1)
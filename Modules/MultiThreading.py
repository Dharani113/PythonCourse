# # # Threads in python are an entity within a process that can be scheduled
# # # for execution. In simpler words, a thread is a computation process that is to be
# # # performed by a computer. It is a sequence of such instructions within
# # # a program that can be executed independently of other codes.
# #
# # from time import sleep
# # from threading import *
# #
# # class Hello(Thread):
# #    def run(self):
# #          for i in range(3):
# #             print("Hello",current_thread().getName())
# #             sleep(1)
# #
# # class Goodmorning(Thread):
# #    def run(self):
# #       for i in range(3):
# #          print("Goodmorning",current_thread().getName())
# #          sleep(1)
# #
# # p1 = Hello()
# # p2 = Goodmorning()
# #
# # p1.start()
# # sleep(0.2)
# # p2.start()
# # p1.join()
# # p2.join()
# # print("bye",current_thread().getName())
# #
# # # 2.without classmethod::
# #
# # from threading import *
# #
# #
# # def new():
# #     for x in range(6):
# #         print("dharani reddy", current_thread().getName())
# #
# #
# # t1 = Thread(target=new)----------(why we create object.and why we used target)
# # print(current_thread().getName())
# # t1.start()
# # t1.join()
# # print("bye", current_thread().getName())
# #
# #
# # 3.without extending thread class::
# from threading import *
# class ex:
#    def B(self):
#       list=[1,2,3,4,5]
#       for x in list:
#        print("number",x,current_thread().getName())
# obj=ex()
# t1=Thread(target=obj.B())
# t1.start()
# t1.join()
# print("bye",current_thread().getName())


import time
def d2(n):
   for x in n:
    print(x%2)
    time.sleep(1)
def d3(n):
   for x in n:
      print(x%3)
      time.sleep(1)
n=[1,2,3,4,5,6,7,8,9]
s=time.time()
d2(n)
d3(n)
d=time.time()
print(d-s)
# from threading import *
# import time
# def d2(n):
#    for x in n:
#       print(x%2)
#       time.sleep(1)
# def d3(n):
#    for x in n:
#       print(x%3)
#       time.sleep(1)
# n=[1,2,3,4,5,6,7,8,9]
# s=time.time()
# t1=Thread(target=d2,args=(n,))
# t2=Thread(target=d3,args=(n,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# e=time.time()
# print(e-s)



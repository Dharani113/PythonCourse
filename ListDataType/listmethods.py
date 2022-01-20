# #list append::(means adding)
# l1=[345,"abs",True,123.33]
# L2=[90,89,'KKK']
# l1.append(L2)
# print(l1)       #ans:[345, 'abs', True, 123.33, 90,89,'KKK']
#
# #COUNT METHOD::
# l2=[123,456,456,"tue",123]
# print(l2.count(123))                           #ANS:2
# print("Count for [123]:",l2.count(123))        #ANS:Count for [123]: 2
# print("Count for tue:",l2.count("tue"))        #ANS:1
# print("count for [456]:",l2.count(456))        #ANS:2
#
# #LIST EXTEND METHOD::
# l3=[123,456,456,"tue",123]
# print(l3)
# l4=[78,90,"hgghh",True,567.566]
# l3.extend(l4)
# print(l3)
#
# #LIST INDEX METHOD::
# l4=[123,345,'tyr']
# print(l4.index(345))                         #ANS::1
# print("index for [l4]:",l4.index(345))       #ans:index for [l4]: 1
#
# #LIST INSERT METHOD::
# l1=[123,456,456,"tue",123]
# l1.insert(9,32111)
# print(l1)
#
# #LIST POP METHOD::
# l1=[123,456,456,"tue",123]
# print("l1:",l1.pop(-2))               #ANS::[123,456,456,123]
#                                       # "tue" will be removed from these parameters
#
# print("l1:",l1.pop(-2))               #ANS::[123,456,123]
#                                     # "456" will be removed from these parameters

 #LIST REMOVE METHOD::
# l5=[123,456,456,"tue",123]
# l5.remove(456)
# print("l5:",l5)
# print(len(l5))

#LIST REVERSE METHOD::
# l6 = [123, 456, 456, "tue", 123]
# l6.reverse()
# print("l6:",[l6])                  #ans:l6: [[123, 'tue', 456, 456, 123]]

#LIST SORT METHOD::
l6 = [123, 456, 456]
l6.sort()
print("l6:",l6)                         #ans:[123,456,456]
l7=["zec","tue"]
l7.sort()
print("l7:",l7)                        #ans:l7: ['tue', 'zec']





# Date object representing date in Python
from datetime import date
# my_date=date(1996,11,10)
# print(my_date)
 # Get Current Date
# today=date.today()
# print(today.year)
# print(today.month)
# print(today.day)

#
#
# #Example 4: Get date from Timestamp
# from datetime import datetime
# date_time=datetime.fromtimestamp(1523319438)
# print(date_time)

#
# # Convert Date to String::
# today=date.today()
# str=date.isoformat(today)
# print(type(str))
from datetime import time
mytime=time()
print(mytime)
# mytime=time(12,23,45,34)
# print(mytime)
#
# mytime=time(hour=1,minute=12)
# print(mytime)
# time=time(12,34,54)
# print(time.hour)
# print(time.minute)
# print(time.second)
# print(time.microsecond)
# from datetime import date
# # today=datetime.now()
# # print(today)
# today=time()
# print(today)



from datetime import datetime
today=time(12,34,54)
print(today)
today=datetime.now()
print(today)


#
import re

import self as self

# text = "7036560930"
# patteren = re.compile(r"(\d{10})")
# print(patteren.search(text).group())
import re
str ="1-800-555-7777"
patteren2 = re.compile("^(\d{1})\D+(\d{3})\D+(\d{3})\D+(\d{4})$")
result =patteren2.search(str).groups()
print(result)
#
# patteren3 = re.compile(r'^\D*(\d{1})\D*(\D{3})\D*(\d{3})\D*(\d{4})$')
# print(patteren3.search(str).group())


# import re
#
# htmlString = '</dd><dt> Fine, thank you.&#160;</dt><dd> Molt bé, gràcies. (<i>mohl behh, GRAH-syuhs</i>)'
#
# SearchStr = '(\<\/dd\>\<dt\>)+ ([\w+\,\.\s]+)([\&\#\d\;]+)(\<\/dt\>\<dd\>)+ ([\w\,\s\w\s\w\?\!\.]+) (\(\<i\>)([\w\s\,\-]+)(\<\/i\>\))'
#
# Result = re.search(SearchStr.decode('utf-8'), htmlString.decode('utf-8'), re.I | re.U)
#
# print(Result.groups())

# str="18005557777"
# patteren2=re.compile(r"(\d{10}")
# result=patteren2.search(str)
# print(result.groups())

# import re
# str="my name is Dharani my age is 25"
# x=re.findall("\s+[a-h-Z]",str)
# print(x)

# dharani13@gmail.com
import re

# pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
# user_id = input("enter the email id")
# if re.search(pattern, user_id):
#     print("valid email id")
# else:
#     print("not ok")
#
#
pattern = '^[a-z 0-9_\-\.]+[@][a-z]+[\.][a-z]{2,3}$'
user_id = input("enter the email id")
if re.search(pattern, user_id):
    print("valid email id")
else:
    print("not ok")




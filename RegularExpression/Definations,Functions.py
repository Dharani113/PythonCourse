#Def:Reg Ex is a sequence of characters that forms a search pattern.
#To specify regular expressions metacharaters are used.
#metacharacters are special meaning.

#FUNCTIONS::
# findall---------->To find duplicates for specied pattern.
# search----------->To test the specified pattern present or not in the given string.
# split------------>Returns a list where the string has been split at each match
# sub-------------->Replaces one or many matches with a string
# Compile--------->Used to create pattern object and can be re used.
# Match----------> To test the input string with specified or not.First position only it will find out.


# EXAMPLES::
# 1.MATCH:
# A.
# import re
# source="my name is dharani,my age is @25"
# pattern="my"
# match = re.match(pattern,source)
# print(match)                       ###ANS:MY

# # B.
# txt = "The rain in Spain"
# x = re.match("rain", txt)
# print(x)                     ##ANS:NONE

# 2.SEARCH::
import re
# # source="my name is dharani,my age is @25"
# # pattern="dharani"
# # match = re.search(pattern,source)
# # print(match)
# # #ANS:<re.Match object; span=(11, 18), match='dharani'>

# source="my name is dharani,my age is @25"
# pattern="my"
# match =re.search(pattern,source)
# print(match)
# #ANS:NONE


# # 3.FINDALL::
# source="my name is dharani,my age is @25"
# pattern="my"
# findall =re.findall(pattern,source)
# print("findall:",findall)
# # ANS:findall: ['my', 'my']

#4.SPLIT::
# source="my name is dharani,my age is @25"
# pattern="is"
# split =re.split(pattern,source)
# print("split:",split)
# # ANS:split: ['my name ', ' dharani,my age ', ' @25']

#5.REPLACE or SUB:
source="my name is dharani,my age is @25"
pattern="dharani"
replace =re.sub(pattern,'dhatri',source)
print("replace:",replace)






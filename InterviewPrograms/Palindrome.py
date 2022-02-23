# a word, phrase, or sequence that reads the same backwards as forwards
# ex:121,242,2112,etc.

# using slicling::
# string = input("enter a string")
# rev_string = string[::-1]
# if string == rev_string:
#     print("palindrome")
# else:
#     print("not palindrome")


# USING LOOP::
str2 = input("enter a string")


def palindrome(str2):
    for i in range(0, int(len(str2) / 2)):
        if str2[i] != str2[len(str2) - i - 1]:
            return False
    return True

ans = palindrome(str2)
if (ans):
    print("yes")
else:
    print("no")



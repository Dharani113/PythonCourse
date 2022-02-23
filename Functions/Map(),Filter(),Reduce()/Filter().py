# Letters=["a","b","d","e","i","h","j","u","o"]
# def filter_vowels(letters):
#     vowels=["a","e","i","o","u"]
#     return True if letters in vowels else False
#
# filter_vowels=filter(filter_vowels, "letters")
# vowels=tuple(filter_vowels)
# print(vowels)
#
# # ages=[12,16,18,24]
# # def vote(x):
# #     if x>=18:
# #         print("eligible for vote")
# #     else:
# #         print("not eligible")
# # adults=filter(vote,ages)
# # for x in adults:
# #     print(x)
#
# # letters=["a","b","d","e","i","h","j","u","o"]
# # def filter_nonvowels(letters):
# #     vowels=["a","e","i","o","u"]
# #     if(letters in vowels):
# #         return False
# #     else:
# #         return True
# # filter_nonvowels=filter(filter_nonvowels,letters)
# # print(list(filter_nonvowels))
# #
# #
#
#
# l = [1, 2, 3, 4, 5, 6, 8, 9]
# list = list(filter(lambda x: x % 2, l))
# print(list)

letters=["a","b","d","e","i","h","j","u","o"]
def filter_vowels(letters):
    vowels = ["a", "e", "i", "o", "u"]
    if(letters in vowels):
        print("all vowels")
    else:
        print("no vowels")
filter_nonvowels=filter(filter_nonvowels,lwtters)

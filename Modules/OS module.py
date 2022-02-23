# #                  #1. Getting the Current working directory::
# # # To get the location of the current working directory os.getcwd() is used.
# # import os
# # cwd=os.getcwd()
# # # print("current working directory",cwd)
# # # ANS:current working directory C:\Users\otr17\PycharmProjects\PythonCourse\Modules
# #
# #                    # 2.Changing the Current working directory::
# # import os
# # def currenr_path():
# #     print("before changing directory")
# #     print(os.getcwd())
# # currenr_path()
# # print("after changing directory")
# # os.chdir('../')
# # currenr_path()
#
#                         #3.Creating a Directory
#                             # 1.os.mkdir()
#                             # 2.os.makedirs()
#
# # 1.os.mkdir():
# import os
# directory = "GeeksforGeeks"
# parent_dir = "D:"
# path=os.path.join(parent_dir,directory)
# os.mkdir(path)
# print(directory)



# #4.listingout files & directories with python:
import os
path="/"
dir_list=os.listdir(path)
print(path,"/:")
print(dir_list)
size=os.path.getsize("D:")
print(size,"bytes.")



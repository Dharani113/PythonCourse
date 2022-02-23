filename = "C:\\Users\\otr17\\PycharmProjects\\PythonCourse\\Python PracticeFolder\\FilehandlinfPractise\\demofile.txt"
# f = open(filename, "w")
# str = "my name is dharani reddy"
# f.write(str)
# read a file using open() and close()
# f = open(filename)
# print(f.read())
# f.close()

# # read a file using with statement, auto close the opened file
# with open(filename) as f:
#     print(f.read())

# read a file using try-finally
# f = open(filename)
# try:
#     print(f.read())
# finally:
#     f.close()


# read a file line by line
# with open(filename) as f:
#    lines = f.readlines()
#    for line in lines:
#        # print(line)
#        print(line, end='') # prevent add a new line

# skip the first line
# line = []
# with open(filename) as f:
#    line = f.readlines()[-3] # skip the first line
# #
# print(line)


# r+
with open(filename, 'r+') as f:
   f.seek(0)
   print(f.readlines())                   # move fp to end of the file
   f.write("new line \n")












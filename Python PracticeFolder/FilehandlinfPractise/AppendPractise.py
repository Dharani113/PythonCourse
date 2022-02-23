filename = "C:\\Users\\otr17\\PycharmProjects\\PythonCourse\\Python " \
           "PracticeFolder\\FilehandlinfPractise\\AppendPractise.txt "

# append to a file
with open(filename, 'a+') as f:
    f.write("a new line")
    f.seek(10)
    print(f.read())

# read and append to a file, a+
# with open(filename, 'a+') as f:
#     f.seek(0)  # a+ file pointer at end, move to beginning
#     lines = f.readlines()
#     f.write("hello\n")  # append number of lines to a file
#     print(str(len(lines)))

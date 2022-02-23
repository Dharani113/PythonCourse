import sys
print(sys.path)
print(sys.version)
# print(sys.setrecursionlimit(600))
# print(sys.getrecursionlimit())
#Input and Output using sys::
# 1.stdin
# 2.stdout
# 3.stderr

#1.stdin::
# It can be used to get input from the command line directly.
# It used is for standard input. It internally calls the input() method.
# It, also, automatically adds ‘\n’ after each sentence.






# print(sys.stdout.write('Geek'))

import sys


def print_to_stderr(*a):
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file=sys.stderr)


print_to_stderr("Hello World")

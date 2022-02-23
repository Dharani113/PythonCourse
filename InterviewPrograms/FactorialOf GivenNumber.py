# USING FOR LOOP::
# def factorial(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial = factorial*i
#     return factorial
# result=factorial(6)
# print(result)

# USING RECURSION::
def recursive_func(n):
    if n == 1:
        return n
    else:
        return n * recursive_func(n - 1)


fact = recursive_func(3 )
print(fact)


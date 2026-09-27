# factorial.py

#
# Prints 1 * 2 * 3 * ... * n, where n is a positive integer passed as a
# parameter.
#

def print_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)

print_factorial(52)

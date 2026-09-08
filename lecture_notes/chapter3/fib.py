# fib.py

#
# Prints Fibonacci numbers using a for-loop
#
#
# For the Fibonacci numbers, the first two numbers are 1, and after that each
# number is the sum of the two before it:
#
#   1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#

a, b = 1, 1
for i in range(10):
    print(a)
    prev_a = a
    a = b
    b = prev_a + b
    # a, b = b, a + b

# digitsum.py

#
# Write a program that prints all the numbers from 100 to 999 that are evenly
# divisible by the sum of its digits.
#
# For example, 540 is printed because the sum of its digits is 5 + 4 + 0 = 9,
# and 540 is a multiple of 9.
#
# Hint: There are 180 numbers in total: 100, 102, 108, …,  990, 999.
#

for n in range(100, 1000):
    # n has the form abc, where a, b, and c are digits
    c = n % 10
    b = (n // 10) % 10
    a = n // 100
    sum_of_digits = a + b + c
    if n % sum_of_digits == 0:
        print(n)

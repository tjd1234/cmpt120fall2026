# q2_sol.py

"""
Write a program that reads a positive integer n from the user, and then prints
all the prime numbers less than n, followed by the total number of primes found.

As part of your program, define and use a function called `is_prime(n)` that
returns `True` if `n` is prime, and `False` otherwise.

A number is prime if it is in an integer greater than 1 that has no positive
divisors other than 1 and itself. The first few primes are 2, 3, 5, 7, 11, ....

```
Enter a positive integer: 100

The prime numbers less than 100 are: 
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 

Total number of primes less than 100: 25
```
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input('Enter a positive integer: '))
print(f'\nThe prime numbers less than {n} are: ')
prime_count = 0
for i in range(2, n):
    if is_prime(i):
        print(i, end=' ')
        prime_count += 1
print()
print()
print(f'Total number of primes less than {n}: {prime_count}')

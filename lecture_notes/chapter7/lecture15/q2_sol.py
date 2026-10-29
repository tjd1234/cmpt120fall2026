# q2_sol.py

"""
Rewrite the `is_prime` function so it uses a while loop instead of a for loop.
Test it with the given testing code (you can keep the for-loop for the testing 
code --- or rewrite it to a while loop for extra practice).

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#
# test code
#
n = 1000  # 25 primes less than 100, 168 primes less than 1000
num_primes = 0
for i in range(2, n):
    if is_prime(i):
        print(i, end=' ')
        num_primes += 1

print()
print()
print(f'Total number of primes less than {n}: {num_primes}')
```

"""

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

#
# test code
#
n = 1000  # 25 primes less than 100, 168 primes less than 1000
num_primes = 0
for i in range(2, n):
    if is_prime(i):
        print(i, end=' ')
        num_primes += 1
print(f'\n\nTotal number of primes less than {n}: {num_primes}')

# q2.py

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

# q3.py

"""
Write a program that asks the user to enter a positive integer `n`, and then
prints the sum of `1 + 2 + 3 + ... + n` in three different ways:

1. Using the formula: n(n+1)/2. Put this in a function called `sum_formula(n)`
   that returns (not prints!) the result.

2. Using a for loop. Put this in a function called `sum_loop(n)` that returns
   (not prints!) the result.

3. Using this recursive formula: if `n` is `1`, then return `1`. Otherwise,
   return `n + sum_recursive(n-1)`. Put this in a function called
   `sum_recursive(n)` that returns (not prints!) the result.

```
What is n? 5

  sum_formula(5) returns 15
     sum_loop(5) returns 15
sum_recursive(5) returns 15
```

All the returned numbers should be the same.

Note that the recursive one might fail if `n` is too large, e.g. try running it
with `n = 1000`.
"""

n = 5
sum_formula = (n * (n + 1)) // 2  # 3 operations: *, +, //

print(f'sum_formula({n}) returns {sum_formula}')

# for-loop: n operations: += each time through the loop
total = 0
for i in range(1, n + 1):
    total += i

print(f'   sum_loop({n}) returns {total}')







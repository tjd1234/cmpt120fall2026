# fibonacci.py

def F(n):
    """Returns the nth Fibonacci number.
    """
    if n == 0:   # base case 1
        return 0
    elif n == 1: # base case 2
        return 1
    else:        # recursive case
        return F(n - 1) + F(n - 2)

# for i in range(10+1):
#     print(f'Calculating F({i})...', end='')
#     print(f'{F(i)}')







def F_loop(n):
    """Returns the nth Fibonacci number.
    """
    a = 0
    b = 1
    for i in range(n):
        a_old = a
        b_old = b
        a = b_old
        b = a_old + b_old
    return a

for i in range(500+1):
    print(f'Calculating F_loop({i})...', end='')
    print(f'{F_loop(i)}')

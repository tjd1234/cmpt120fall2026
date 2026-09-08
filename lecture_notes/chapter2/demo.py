# demo.py

a = 3
b = a * str(a)  # 3 * str(3) == 3 * '3' == '333'
b = len(b) + 3  # len('333') + 3 == 3 + 3 == 6

print(abs(a-b)) # abs(3-6) == abs(-3) == 3

# a: 3
# b: 6
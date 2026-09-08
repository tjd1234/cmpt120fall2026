# quiz_sol.py

# 1. In the random module, there’s a function called random() that, when called
#    returns a number from 0.0 to 1.0. Write a function called make_list(n) that
#    returns of list of n random numbers from 0.0 to 1.0.


import random
def make_list(n):
    result = []
    for i in range(n):
        result.append(random.random())
    return result



# 2. Write a program that asks the user an integer n (assume it is always valid
#    and greater than 0), makes a list of n random numbers from 0.0 to 1.0, and
#    then prints, arranged from smallest to biggest, just the numbers in the
#    list that are less than 0.5. Use the function from above to help (you don’t
#    need to re-write it).

n = int(input('Enter an int: '))
lst = make_list(n)
lst.sort()

for x in nums:
    if x < 0.5:
        print(x)

# more efficient alternative:
# i = 0
# while i < n and lst[i] < 0.5:
#     print(lst[i])
#     i += 1

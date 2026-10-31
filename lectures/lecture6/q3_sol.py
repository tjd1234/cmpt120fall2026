# q3_sol.py

"""
Write a program that asks the user how many sides they would like their die to
have, and then rolls the die 3 times and prints the results of each roll.

```
How many die sides? 6
Rolling a 6-sided die three times ...
1st roll: 6
2nd roll: 5
3rd roll: 2
```

"""
import random

sides = int(input('How many die sides? '))
print(f'Rolling a {sides}-sided die three times ...')
print('1st roll:', random.randint(1, sides))
print('2nd roll:', random.randint(1, sides))
print('3rd roll:', random.randint(1, sides))
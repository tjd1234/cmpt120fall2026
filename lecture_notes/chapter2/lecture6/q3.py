# q3.py

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

sides = int(input('How many sides? '))

print(f'Rolling a {sides}-sided die three times ...')
roll1 = random.randint(1, sides)
roll2 = random.randint(1, sides)
roll3 = random.randint(1, sides)

print('1st roll:', roll1)
print('2nd roll:', roll2)
print('3rd roll:', roll3)

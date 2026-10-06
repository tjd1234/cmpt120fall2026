# q3.py

"""
Write a function called print_in_bars(word) that prints word surrounded by |
characters as shown. This function only prints, and so has no return. Then ask
the user to enter their three favourite foods, and use print_in_bars to print
each food. 

```
Food 1: peaches
Food 2: sushi
Food 3: ice cream

|peaches|
|sushi|
|ice cream|
```
"""
def print_in_bars(word):
    #print('|' + word + '|')
    print(f'|{word}|')

food1 = input('Food 1: ')
food2 = input('Food 2: ')
food3 = input('Food 3: ')
print()
print_in_bars(food1)
print_in_bars(food2)
print_in_bars(food3)

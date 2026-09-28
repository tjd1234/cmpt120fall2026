# q1_sol.py

"""
Make a Python version of the math function f(x) = 2x + 1. Use it print the
values f(2), f(5), and f(1000). Then ask the user to enter a number and print
the value of f(x) as shown.

```
5
11
2001
Enter a number: 2.6
f(2.6) = 6.2
```
"""

def f(x):
    return 2 * x + 1

print(f(2))
print(f(5))
print(f(1000))

x = float(input("Enter a number: "))
print(f'f({x}) = {f(x)}')
# q2_sol.py

"""
Write a function that takes a person's name as input, and returns a string of
the form 'Hello, <name>!'. Then ask the user to enter the names of two people,
and print the result of calling the function for each person.
```
Person 1: Audrey
Person 2: Ali

Hello, Audrey!
Hello, Ali!
```

"""

def make_greeting(name):
    return f'Hello, {name}!'

name1 = input("Person 1: ")
name2 = input("Person 2: ")
print()
print(make_greeting(name1))
print(make_greeting(name2))
# q3_sol.py

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
    print(f'|{word}|')

food1 = input("Food 1: ")
food2 = input("Food 2: ")
food3 = input("Food 3: ")
print()
print_in_bars(food1)
print_in_bars(food2)
print_in_bars(food3)
# q4_sol.py

"""
Write a function called print_in_box(word) that prints word in a box as shown.
Use the print_in_bars function from the previous question to print the middle
line of the box. Then ask the user to enter a movie name and print in a box.

```
Enter a movie name: The Matrix
+----------+
|The Matrix|
+----------+
```
"""

def print_in_bars(word):    
    print(f'|{word}|')

def print_in_box(word):
    bar = '+' + '-' * len(word) + '+'
    print(bar)
    print_in_bars(word)
    print(bar)


movie = input("Enter a movie name: ")
print_in_box(movie)
# q5_sol.py

"""
Write a program that asks the user to enter an int that is 0 or greater, and a
word, and then prints the word in a numbered list as shown. Use a for-loop in
your solution. No functions are required, but you can make one if you want.

```
Enter an int: 3
Enter a word: hello!
hello!
hello!
hello!
```
"""

n = int(input("Enter an int: "))
word = input("Enter a word: ")
print()
for i in range(n):
    print(f'{i+1}. {word}')
# q6_sol.py

"""
Write a program that asks the user to enter an int (called n)that is 0 or
greater. Then, starting at 1, print the ints from 1 to n on the screen in a box
as shown. Use the print_in_box(word) function from the previous question.

```
Enter an int: 3

+-+
|1|
+-+

+-+
|2|
+-+

+-+
|3|
+-+
```
"""

def print_in_bars(word):    
    print(f'|{word}|')

def print_in_box(word):
    bar = '+' + '-' * len(word) + '+'
    print(bar)
    print_in_bars(word)
    print(bar)

n = int(input("Enter an int: "))
print()
for i in range(1, n+1):
    print_in_box(str(i))
    print()

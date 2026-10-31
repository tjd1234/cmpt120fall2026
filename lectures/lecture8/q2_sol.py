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

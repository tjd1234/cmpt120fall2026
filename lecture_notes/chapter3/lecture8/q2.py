# q2.py

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
def hello_string(name):
    return f'Hello {name}!'

person1 = input('Person 1: ')
person2 = input('Person 2: ')
print()
print(hello_string(person1))
print(hello_string(person2))

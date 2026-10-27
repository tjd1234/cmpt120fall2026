# q4.py

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

def print_in_box(s):
    bar = '+' + len(s) * '-' + '+'
    #print(word)
    #print(len(word))
    #bar = 'bar'
    print(bar)
    print_in_bars(s)
    print(bar)

title = input('Movie name: ')
print()
print_in_box(title)

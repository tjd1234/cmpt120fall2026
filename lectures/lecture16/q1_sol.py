# q1_sol.py

"""
Write a program that prints the contents of a text file to the screen, numbering
each line.

For example, suppose groceries.txt contains the following:

```
eggs
milk
coffee
more coffee
chocolate
```

Then:

```
What file would you like to print? groceries.txt

1. eggs
2. milk
3. coffee
4. more coffee
5. chocolate
```
"""

filename = input('What file would you like to print? ')
print()

input_file = open(filename, 'r')  # 'r' means open the file for reading only

line_number = 1
for line in input_file:
    print(f'{line_number}. {line.strip()}')  # strip() removes the newline character
    line_number += 1

input_file.close()

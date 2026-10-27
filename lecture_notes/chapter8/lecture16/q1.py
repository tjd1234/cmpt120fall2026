# q1.py

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

#filename = input('Enter file: ')
filename = 'groceries.txt'

input_file = open(filename, 'r')  # 'r' means for reading

line_number = 1
for line in input_file:
    line = line.strip()
    print(f'{line_number}. {line}')
    line_number += 1


    



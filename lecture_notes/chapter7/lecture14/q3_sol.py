# q3_sol.py

"""
Write a program that reads the lines of the file groceries.txt and prints each
line on the screen starting with a number.

For example, suppose groceries.txt contains the following:

```
eggs
milk
coffee
more coffee
chocolate
```

Then your program should print:

```
1. eggs
2. milk
3. coffee
4. more coffee
5. chocolate
```

You can assume that the file groceries.txt is in the same directory as your
program, and could contain 0 or more lines.
"""

#
# open the file; the 'r' means to open it for reading only
#
input_file = open('empty.txt', 'r')

# print each line on the screen starting with its line number
line_number = 1
for line in input_file:
    print(f"{line_number}. {line.strip()}")
    line_number += 1

#
# close the file
#
input_file.close()

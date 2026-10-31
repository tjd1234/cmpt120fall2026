# q4_sol.py

"""

Write a shopping list program where the user is asked to enter the name of a
file they want to write to, and then repeatedly asks the user to enter grocery
list items. Each item should be written to the file on its own line. The program
should stop when the user presses <enter> without typing an item.


Sample Run

```
What file do you want to write to? list.txt
Enter an item: apples
Enter an item: bananas
Enter an item: carrots
Enter an item: <enter>

Done!
See list.txt for your list.
```

"""
filename = input('What file do you want to write to? ')
outfile = open(filename, 'w') # 'w' for writing to the file

item = input('Enter an item: ').strip()
while item != '':
    outfile.write(item + '\n') # \n ends a line in the file
    item = input('Enter an item: ').strip()
outfile.close()

print('Done!')
print(f'See {filename} for your list.')

# q3.py

"""
Write a program that asks the user for the following information:

- the name of a file they would like to create
- a list of names they would like to appear in the file, e.g. the user might
  enter the five names "Ava Ben Cara Dana Evan"
- ask for how many names they want in the file

After getting this information, the program should create a file with the given
name and then fill it with random names (from the user's list) until the file
contains the specified number of names. Each name should be on its own line.

Hint: import the random module, and use random.choice() to select random names
from the list.

Sample Run

```
What file? votes.txt
What names? Ava Ben Cara Dana Evan 
How many names in the file? 100

Okay, created votes.txt with 100 random names.
```

Now the file votes.txt should exist and contain 100 random names, e.g. starting
like this:

```
Dana
Dana
Ava
Cara
Evan
Ava
Evan
Ben
Ava
Ava
...
```

There should be exactly 100 names in random order.
"""

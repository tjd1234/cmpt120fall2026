# q1_sol.py

"""
Make a fortune cookie program that, when run, randomly prints one of these
phrases:

- Whatever you do, always give 100% — unless you're donating blood.
- Be a cupcake in a world full of muffins.
- We become what we think about: so don't think too much about hot dogs.
- You can’t have everything. Where would you put it?

Sample run 1
```
Be a cupcake in a world full of muffins.
```

Sample run 2
```
You can't have everything. Where would you put it?
```

Sample run 3
```
Be a cupcake in a world full of muffins.
```

Since the program chooses the quote randomly, there will be repeats across
different runs.

"""

import random

n = random.randint(1, 4)
if n == 1:
    print("Whatever you do, always give 100%—unless you're donating blood.")
elif n == 2:
    print("Be a cupcake in a world full of muffins.")
elif n == 3:
    print("We become what we think about: so don't think too much about hot dogs.")
elif n == 4:
    print("You can't have everything. Where would you put it?")

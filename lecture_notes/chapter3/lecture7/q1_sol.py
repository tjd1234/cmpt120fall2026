# q1_sol.py

"""
Pat, Chris, Blake, and Robin all love dolls. Pat and Chris have some number of
dolls (entered by the user), while the number of dolls Blake and Robin have
follow these rules:

- Blake has two dolls, plus three times as many as Pat.
- Robin has one more doll than whoever of Pat and Chris has the most dolls.

Write a program that gets the number of dolls for Pat and Chris, and then prints
how many dolls each person has, plus the total number of dolls overall.

```
Dolls for Pat: 3 
Dolls for Chris: 5

Pat has 3 dolls. 
Chris has 5 dolls. 
Blake has 11 dolls. 
Robin has 6 dolls.
Total number of dolls: 25
```
"""
# get the number of dolls for Pat and Chris
pat_dolls = int(input("Dolls for Pat: "))
chris_dolls = int(input("Dolls for Chris: "))

# calculate the number of dolls for Blake and Robin
blake_dolls = 2 + 3 * pat_dolls
robin_dolls = 1 + max(pat_dolls, chris_dolls)
total_dolls = pat_dolls + chris_dolls + blake_dolls + robin_dolls

# print the number of dolls for each person
print()
print(f"Pat has {pat_dolls} dolls.")
print(f"Chris has {chris_dolls} dolls.")
print(f"Blake has {blake_dolls} dolls.")
print(f"Robin has {robin_dolls} dolls.")
print(f"Total number of dolls: {total_dolls}")

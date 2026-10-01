# q4_sol.py

"""
Write a program that asks the user to enter an int that is greater than 1, and
then prints a countdown from that int to 1, finally printing "Blastoff!".

```
Enter an int: 5
5
4
3
2
1
Blastoff!
```
"""

start = int(input("Enter an int: "))
for i in range(start):
    print(start - i)
print("Blastoff!")

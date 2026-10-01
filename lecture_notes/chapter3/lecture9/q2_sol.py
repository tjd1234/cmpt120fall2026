# q2_sol.py

"""
Write a program that asks the user to enter an int that is 0 or greater, and a
word, and then prints the word in a numbered list as shown. Use a for-loop in
your solution. No functions are required, but you can make one if you want.

```
Enter an int: 3
Enter a word: hello!
hello!
hello!
hello!
```
"""

n = int(input("Enter an int: "))
word = input("Enter a word: ")
print()
for i in range(n):
    print(f'{i+1}. {word}')

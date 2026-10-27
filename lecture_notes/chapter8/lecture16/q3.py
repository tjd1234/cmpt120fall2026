# q3.py

"""
Write a program that reads a string from the user and then prints the letter and
index value in the style shown.

0 1 2 3 4 5
h e l l o ?

```
Enter a string: hello

s = 'hello'
s[0] is 'h'
s[1] is 'e'
s[2] is 'l'
s[3] is 'l'
s[4] is 'o'
```
"""
s = 'Star Wars 3'
print(f"s = '{s}'")
for i in range(len(s)):
    c = s[i]
    #print(i, c)
    print(f"s[{i}] is '{c}'")

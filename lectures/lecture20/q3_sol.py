# q3_sol.py

"""
The file trails.txt contains the names of some local hiking trails. The parks
department wants to make trail signs all the same width, and so they need to
know the longest trail name.

Write a program that opens trails.txt and then prints the longest trail name,
plus its length. The length should include any spaces in the name, but not
newlines or other whitespace characters.

Your program should work with any number of trails in the file.

Sample Run

```
Longest trail name: Baden-Powell Trail (18 characters)
```
"""

all_trails = open('trails.txt')
longest_trail = ''
for trail in all_trails:
    trail = trail.strip()
    if len(trail) > len(longest_trail):
        longest_trail = trail

print(f"Longest trail name: {longest_trail} ({len(longest_trail)} characters)")
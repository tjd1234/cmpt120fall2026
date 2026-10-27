# q2_sol.py

"""
Write a program that finds and prints all the English words that don't have a
vowel. The vowels are a, e, i, o, u, and y, and use words.txt as the list of
English words.

```
1. crwth
2. crwths
3. cwm
4. cwms
5. nth
...
14. tsktsks
```
"""
def has_vowel(word):
    for vowel in 'aeiouy':
        if vowel in word:
            return True
    return False

#
# open the words file and read it line by line
#
words_file = open('words.txt', 'r')
num = 0
for word in words_file:
    word = word.strip()
    if not has_vowel(word):
        num += 1
        print(f'{num}. {word}')

words_file.close()

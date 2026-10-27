# q2.py

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
def has_vowel(s):
    for char in s:
        if char in 'aeiouy':
            return True
    return False

#def has_vowel(s):
#    for vowel in 'aeiouy':
#        if vowel in s:
#            return True
#    return False


word_file = open('words.txt', 'r')
word_num = 1
for word in word_file:
    word = word.strip()
    if not has_vowel(word):
        print(f'{word_num}. {word}')
        word_num += 1
#    if has_vowel(word):
#        pass
#    else:
#        print(f'{word_num}. {word}')
#        word_num += 1


    

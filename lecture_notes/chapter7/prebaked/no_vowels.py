# no_vowels.py

def has_vowel(word):
    for c in word.lower():
        if c in 'aeiou':
            return True
    return False

file_object = open('words.txt')

non_vowel_words = 0
for line in file_object:
    if not has_vowel(line):
        non_vowel_words += 1

print(f'{non_vowel_words} words have no vowels')

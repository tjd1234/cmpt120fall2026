# counting_chars.py
# Counting Letters in Strings
#
# This file shows how to use dictionaries to count the letters in a string.


## Method 1: Predefined Letters

# TODO 1: Make a dictionary with 26 key:value pairs, where
# the keys are 'a', 'b', 'c', etc. up to 'z', and the values are 0.
# Print the dictionary to verify it's correct.
letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
           'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
           's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
print(letters)
print(letters.keys())   # a, b, c, etc.
print(letters.values()) # 0, 0, 0, etc.

# TODO 2: Using a for-loop, loop through the letters of the string 'applesauce' and
# for each letter add 1 to the corresponding count. Print the dictionary to verify
# it's correct.
str = 'applesauce'
for c in str:
    letters[c] += 1

print(letters)

# TODO 3: Print just the letters and counts that have a count greater than 0.
for c in letters:
    if letters[c] > 0:
        print(c, letters[c])

# TODO 4: Use a loop to re-initialize letters so all the counts are 0 again.
for c in letters:
    letters[c] = 0

print(letters)

# TODO 5: Using a for-loop, loop through the letters of the string 'hello world!' and
# for each letter add 1 to the corresponding count. Print the dictionary to verify
# it's correct.
str = 'hello world!'
for c in str:
    if c in letters:
        letters[c] += 1

print(letters)


## Method 2: Adding Letters as You Go

# TODO 6: Initialize an empty dictionary called letters.
letters = {}

# TODO 7: Loop through the letters of the string 'applesauce' and increment
# the count of that letter by 1. If the letter is not a key in the
# dictionary, first add it and set its value to 0.
#
# Print the dictionary to verify it's correct.
str = 'hello world!'
for c in str:
    if c not in letters:
        letters[c] = 0
    letters[c] += 1

print(letters)

# TODO 8: Re-do the above using the string 'hello world!'.

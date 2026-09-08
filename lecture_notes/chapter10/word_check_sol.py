# word_check.py
# Counting Reverse Words
#
# This file shows two ways to count how many English words are the reverse of
# an English word. It shows a slow way using lists, and a fast way using
# dictionaries.


## The Slow Way: Lists

# TODO 1: Read the words in the file words_short.txt into a list.
# Strip any whitespace from the ends, and make sure there are no
# empty strings. Print the list to verify it's correct.
words = []
for w in open('words_short.txt'):
    w = w.strip()
    if w != '':
        words.append(w)
# print(words)

# TODO 2: Write a for-loop that counts how many words are the reverse of
# some word in the list, and print the count. For example, "tab" is the reverse
# of "bat". Run it with both words_short.txt and words.txt. Follow these steps:
#
# - initialize a count variable to 0
# - loop through the words
# - if the reverse of the current word is in the list, add 1 to the count
# - print the count (it should be 1 for words_short.txt, and 885 for words.txt)
count = 0
for w in words:
    if w[::-1] in words:
        count += 1

print(count)


## The Fast Way: Dictionaries

# TODO 3: Read the words in the file words_short.txt into a dictionary. Print
# the dictionary to verify it's correct.
#
# Use these steps:
# - initialize an empty dictionary
# - loop through the words in the file; make sure to strip whitespace from the
#   ends, and don't add any empty strings
# - add the current word to the dictionary as a key, and set its value to 1,
#   e.g. words[w] = 1
words = {}
for w in open('words.txt'):
    w = w.strip()
    if w != '':
        words[w] = 1

# print(words)

# TODO 4: Write a for-loop that counts how many words are the reverse of some
# word in the dictionary, and print the count. Run it with both words_short.txt
# and words.txt. Follow these steps:
#
# - initialize a count variable to 0
# - loop through the words in the dictionary
# - if the reverse of the current word is in the dictionary, add 1 to the count
# - print the count (it should be 0 for words_short.txt, and 885 for words.txt)
#
# How much faster is it to use a dictionary than a list?
count = 0
for w in words:
    if w[::-1] in words:
        count += 1

print(count)

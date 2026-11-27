# q1_sol.py

"""
Write a program that copies the file words_shuffled.txt into a new filed named
words_sorted.txt, where the words are sorted in alphabetical order. You can
assume that the file.

Print out how many words are in the file.
"""

#
# read the shuffled words into a list
#
shuffled_file = open("words_shuffled.txt", "r")
all_words = []
for word in shuffled_file:
    words = word.strip()
    all_words.append(words)

shuffled_file.close()
print(f'There are {len(all_words)} words in the file.')

#
# sort the words
#
all_words.sort()

#
# write the sorted words to a new file
#
sorted_file = open("words_sorted.txt", "w")
for word in all_words:
    sorted_file.write(word + "\n")
sorted_file.close()
print('Words written to words_sorted.txt')

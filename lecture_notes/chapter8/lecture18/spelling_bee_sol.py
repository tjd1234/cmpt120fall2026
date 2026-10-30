# spelling_bee_sol.py

#
# Question 1
#
# returns True if the word has at least 4 letters, and False otherwise
#
def is_long_enough(word):
    return len(word) >= 4


#
# Question 2
#
# returns True if the word contains the required letter, and False otherwise
#
def has_required(word, required_letter):
    return required_letter in word


#
# Question 3
#
# returns True if each letter in word is also in puzzle_letters, and False
# otherwise
#
def uses_only(word, puzzle_letters):
    for letter in word:
        if letter not in puzzle_letters:
            return False
    return True


#
# Question 4
#
# returns True if every letter in puzzle_letters is in word, and False otherwise
#
def is_pangram(word, puzzle_letters):
    for letter in puzzle_letters:
        if letter not in word:
            return False
    return True


#
# Question 5
#
# returns the score of word for the given required letter and puzzle letters
#
# The scoring rules are:
#
# - words that contain a letter *not* in puzzle_letters score 0 points
# - words that don't contain the required letter score 0 points
# - words less than 4 letters score 0 points
# - words with exactly 4 letters score 1 point
# - words with more than 4 letters score 1 point per letter; if the word is a
#   pangram, then add 7 additional points
#
def word_score(word, required_letter, puzzle_letters):
    if not is_long_enough(word):
        return 0
    elif not has_required(word, required_letter):
        return 0
    elif not uses_only(word, puzzle_letters):
        return 0
    
    if len(word) == 4:
        return 1
    else:
        score = len(word)
        if is_pangram(word, puzzle_letters):
            score += 7
        return score

#
# Use this code to test your word_score function.
#
# puzzle_letters = 'gpdroan'
# required_letter = 'r'
# test_words = ['poor',       # 1
#               'drop',       # 1
#               'droop',      # 5
#               'propaganda', # 17
#               'rap',        # 0
#               'rope',       # 0
#               'pog']        # 0
# for word in test_words:
#     print(word, word_score(word, required_letter, puzzle_letters))


#
# Question 6
#
# Write a program that solves a Spelling Bee puzzle. Do it as follows:
#
#    For each word in words.txt (a list of English words) do the following: 
#       Use word_score to calculate the score of the word. 
#       If the score is greater than 0, then print the word and its score.
#    
#    After all the words have been processed, print the total number words
#    found, and the total sum of all the scores.
#
# For example:
#
#     ... list of words and scores ...
# 
#     Puzzle letters: gpdroan
#    Required letter: r
#        Total words: 76
#        Total score: 306
#


#
# Question 7
#
# Re-do question 6, but now use a list called found_words to keep track of all
# the words found in the puzzle, and the their scores. Initialise the list
# before reading any words like this:
#
#    found_words = []
#
# To add a word and its score to the end of the list, use the append method like
# this:
#
#    found_words.append((score, word))
#
# Now you can print the words sorted by score like this:
#
#    found_words.sort() 
#    for score, word in found_words: 
#       print(score, word)
#

def solution_no_list():
    puzzle_letters = 'gpdroan'
    required_letter = 'r'
    all_words = open('words.txt')
    total_score = 0
    total_words = 0
    for word in all_words:
        word = word.strip()
        score = word_score(word, required_letter, puzzle_letters)
        if score > 0:
            print(word, score)
            total_score += score
            total_words += 1
    print()
    print(f' Puzzle letters: {puzzle_letters}')
    print(f'Required letter: {required_letter}')
    print(f'    Total words: {total_words}')
    print(f'    Total score: {total_score}')

# solution_no_list()

def solution_with_list():
    # puzzle_letters = 'gpdroan'
    # required_letter = 'c'
    puzzle_letters = 'lavcone'  # Fri Oct 30 2026 
    required_letter = 'v'
    all_words = open('words.txt')
    found_words = []
    total_score = 0
    for word in all_words:
        word = word.strip()
        score = word_score(word, required_letter, puzzle_letters)
        if score > 0:
            found_words.append((score, word))
            total_score += score
    found_words.sort()
    for score, word in found_words:
        print(score, word)
    print()
    print(f' Puzzle letters: {puzzle_letters}')
    print(f'Required letter: {required_letter}')
    print(f'    Total words: {len(found_words)}')
    print(f'    Total score: {total_score}')
    
solution_with_list()

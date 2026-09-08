# spelling_bee.py

def pangram_bonus(word, puzzle_letters):
    for c in puzzle_letters:
        if c not in word:
            return 0
    return 7

def word_score(word, required, puzzle_letters):
    if required not in word or len(word) < 4:
        return 0
    
    for c in word:
        if c not in puzzle_letters:
            return 0
    
    if len(word) == 4:
        return 1
    return len(word) + pangram_bonus(word, puzzle_letters)

#
# main program
#
puzzle_letters = 'PLACEIB'
required_letter = 'P'

total_score = 0
scoring_words = 0
file_object = open('words.txt')
for w in file_object:
    w = w.strip().upper()
    
    score = word_score(w, required_letter, puzzle_letters)
    if score > 0:
        total_score += score
        scoring_words += 1
        print(f'{w}, {score} points')

print()
print(f'Total score: {total_score}')
print(f'Total scoring words: {scoring_words}')

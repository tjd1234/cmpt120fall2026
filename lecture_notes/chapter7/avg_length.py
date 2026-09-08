# avg_length.py

def is_m_word(word):
    for c in word:
        if c in 'mM':
            return True
    return False

file_object = open('words.txt')
word_count = 0
num_m_words = 0
for line in file_object:
    if is_m_word(line):
        print(line.strip())
        num_m_words += 1
    word_count += 1

print(f'    Number of words with an "m": {num_m_words}')
print(f'          Total number of words: {word_count}')
print(f'Percentage of words with an "m": {(num_m_words / word_count) * 100:.1f}%')
# m_word_pct.py

file_object = open('words.txt')
total_words = 0
total_m_words = 0
for line in file_object:
    total_words += 1
    if 'm' in line.lower():
        total_m_words += 1

pct = 100 * total_m_words / total_words
print(f'{pct:.1f}% of the words have an "m"')

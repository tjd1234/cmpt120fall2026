# m_word_pct.py

def is_m_word(word):
    for c in word:
        if c in 'mM':
            return True
    return False

def check_if_m_word(word):
    if is_m_word(word):
        print(f'"{word}" has an m')
    else:
        print(f'"{word}" does not have an m')

check_if_m_word('mumble')
check_if_m_word('apple')
check_if_m_word('')

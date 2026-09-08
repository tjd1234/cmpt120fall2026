# same.py

#
# Shows how == for strings could be implemented using a loop and just
# character-by-character comparison.
#
def same(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

def different(s, t):
    return not same(s, t)

def test_same():
    print('testing same ...')
    assert same('hello', 'hello') == True
    assert same('hello', 'ello') == False
    assert same('hello', 'Hello') == False
    assert same('', '') == True
    assert same('', 'a') == False
    print(' ...all same tests passed')

test_same()

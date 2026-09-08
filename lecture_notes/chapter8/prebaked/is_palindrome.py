# is_palindrome.py

#
# Shows how to check if a string is a palindrome using a loop and just
# character-by-character comparison.
#
def is_palindrome1(s):
    a = 0
    b = len(s) - 1
    while a < b:
        if s[a] != s[b]:
            return False
        a += 1
        b -= 1
    return True

def is_palindrome2(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def is_palindrome3(s):
    return s == s[::-1]   # s[::-1] is the reverse of s

def test_is_palindrome(is_palindrome):
    print(f'testing {is_palindrome.__name__} ...')
    assert is_palindrome('') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('aa') == True
    assert is_palindrome('aaa') == True
    assert is_palindrome('baa') == False
    assert is_palindrome('aba') == True
    assert is_palindrome('aab') == False
    assert is_palindrome('racecar') == True
    print(' ...all is_palindrome tests passed')

test_is_palindrome(is_palindrome1)
test_is_palindrome(is_palindrome2)
test_is_palindrome(is_palindrome3)

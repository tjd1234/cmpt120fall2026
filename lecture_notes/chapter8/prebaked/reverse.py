# reverse.py

#
# Shows how to reverse a string using a loop and just
# character-by-character comparison.
#
def reverse1(s):
    result = ''
    for c in s:
        result = c + result
    return result

def reverse2(s):
    result = ''
    for i in range(len(s)):
        result = s[i] + result
    return result

def reverse3(s):
    return s[::-1]

def test_reverse(reverse):
    print(f'testing {reverse.__name__} ...')
    assert reverse('') == ''
    assert reverse('a') == 'a'
    assert reverse('ab') == 'ba'
    assert reverse('abc') == 'cba'
    assert reverse('hello!') == '!olleh'
    assert reverse('racecar') == 'racecar'
    print(f' ...all {reverse.__name__} tests passed')

test_reverse(reverse1)
test_reverse(reverse2)
test_reverse(reverse3)
test_reverse(reverse4)

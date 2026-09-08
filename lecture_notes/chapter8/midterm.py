# midterm.py

# a) (3 marks) Write a function called is_digit(s) that returns True if the
# string s is a single digit, and False otherwise. The digits are '0' through
# '9', and assume s is a string. 
#
# For example:
#    print(is_digit('5'))   # True
#    print(is_digit('52'))  # False
#    print(is_digit('2w0')) # False
#
# In addition:
# •	Do not use the built-in s.isdigit() function in any way.
# •	Do not import anything.
# •	Do not use lists or tuples. Stick to features of Python discussed so far in the course.
# •	Make your function efficient, readable, and short. 
# •	We want to see perfect syntax.

def is_digit(s):
    # return len(s) == 1 and '0' <= s <= '9'
    # return len(s) == 1 and s in '0123456789'
    # return s == '0' or s == '1' or s == '2' or s == '3' or s == '4' ...
    # return s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # if len(s) == 1:
    #     if '0' <= s <= '9':
    #         return True
    # return False
    for d in '0123456789':
        if s == d:
            return True
    return False


# b) (7 marks) Strings s and t are called a good pair just when the following
# things are true:
#
# •	s and t are both non-empty strings of digits (no non-digit characters).
# •	s and t don’t have any digits in common.
#
# Write a boolean function called good_pair(s, t) that returns True if s and t
# are a good pair, and False otherwise. Use is_digit from the previous question
# to help (you don’t need to re-write it), and assume s and t are both strings.
#
# For example:
# print(good_pair('477', '08125'))  # True
# print(good_pair('91234', '56'))   # True
# print(good_pair('477', '5048'))   # False
# print(good_pair('4f7', '08125'))  # False
# print(good_pair('477', ''))       # False
#
# In addition:
#
# •	Do not import anything.
# •	Do not use lists or tuples. Stick to features of Python discussed so far in the course.
# •	Make your function efficient, readable, and short. 
# •	We want to see perfect syntax.

def good_pair(s, t):
    # check for empty strings
    if s == '' or t == '':
        return False

    # check for all digits
    for c in s + t:
        if not is_digit(c):
            return False
    
    # for c in t:
    #     if not is_digit(c):
    #         return False

    # check for digits in common
    # s = '12'  t = '32'
    for d in s:  # check if any digit in s is in t
        if d in t:
            return False
    
    # is this loop necessary?
    for d in t:
        if d in s:
            return False
    
    return True

# list_practice_sol.py

# TODO 1 Write a program that asks the user to enter an int m, then asks the
# user to enter m strings (as shown), and then prints a list of those strings.
# For example:
#
#    Enter an int: 3
#    Enter string 1: cat
#    Enter string 2: shoe
#    Enter string 3: apple
#    ['cat', 'shoe', 'apple']
#
# Assume that the user always types a valid int.

m = int(input('Enter an int: '))
words = []
for i in range(m):
    w = input(f'Enter string {i+1}: ')
    words.append(w)
    
print('initial list:', words)


# TODO 2 Continuing the above program, write code that asks the user to enter an
# int n, and then adds n '!' strings to the end of the list, and then prints it.
# For instance, continuing the above example:
#
#    Enter an int: 2
#    ['cat', 'shoe', 'apple', '!', '!']
#
# Assume that the user always types a valid int. Also, you can make a list with
# multiplication, e.g. ['A'] * 3 is ['A', 'A', 'A'].

n = int(input('Enter an int: '))

for i in range(n):
    words.append('!')

# or instead of a loop:
# words = words + ['!'] * n

print(f'{n} "!" strings added:', words)

# TODO 3 Continuing the above program, write code that asks that user to enter
# an int p, and then adds p '?' strings to the start of the list. For instance,
# continuing the above example where the list is ['cat', 'shoe', 'apple']:
#
#    Enter an int: 3
#    ['?', '?', '?', 'cat', 'shoe', 'apple', '!', '!']
#
# Assume that the user always types a valid int.

p = int(input('Enter an int: '))

for i in range(p):
    words.insert(0, '?')

# or instead of a loop:
# words = ['?'] * p + words

print(f'{p} "?" strings added:', words)

# At this point if you run all the code it should look like this:
#
#    Enter an int: 4
#    Enter string 1: apple 
#    Enter string 2: cherry
#    Enter string 3: pear
#    Enter string 4: banana
#    ['apple', 'cherry', 'pear', 'banana']
#
#    Enter an int: 3
#    ['apple', 'cherry', 'pear', 'banana', '!', '!', '!']
#
#    Enter an int: 2
#    ['?', '?', 'apple', 'cherry', 'pear', 'banana', '!', '!', '!']

# TODO 4 Continuing the above program, now write code that changes the list so
# that it only has '?' and '!' strings, and print the new list.
# 
# For instance, if the list is:
#
#    ['?', '?', 'apple', 'cherry', 'pear', 'banana', '!', '!', '!']
#
# then your code should change it to:
#
#    ['?', '?', '!', '!', '!']
#
# Your code should work for any list of strings created by the above code. 
# 

# p is # of ?s
# n is # of !s
words = p * ['?'] + n * ['!']
print("removed:", words)

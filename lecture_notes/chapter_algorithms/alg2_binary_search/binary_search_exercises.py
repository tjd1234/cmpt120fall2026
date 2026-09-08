# binary_search_exercises.py

#
# Binary search is a search algorithm that finds the index of a target value in
# a list that is in sorted order. It works much faster than linear search.
#
# A list of strings is in sorted if they are in alphabetical order, e.g.:
#
#   in sorted order: ["Alice", "Bob", "Charlie", "Diana", "Eve"] 
#   in sorted order: ["Bob"] 
#   in sorted order: []
#
#   not in sorted order: ["Charlie", "Diana", "Eve", "Alice", "Bob"] 
#   not in sorted order: ["Eve", "Alice"]
#
# A list of numbers is in sorted order if they are in order from smallest to
# largest, e.g.:
#
#   in sorted order: [4, 10, 14, 15]
#   in sorted order: [5] 
#   in sorted order: []
#
#   not in sorted order: [4, 14, 10, 15]
#   not in sorted order: [5, 1]

# TODO 1 Create a new variable called names initialized to this sorted list of
# strings: "Alice", "Bob", "Charlie", "Diana", "Eve". Print it to make sure it
# is correct.
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(names)

# TODO 2 Print the length of names using the len() function.
print(len(names))

# TODO 3 Print the first and last names, and also print the the list in reverse
# alphabetical order.
print(names[0], names[-1], names[::-1])
print(names)


#
# The middle index
#

# TODO 4 Binary search works by checking the middle element of a list. What are
# the middle elements of names? What is the middle element of scores?
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Fred"]
print(names[2])

# TODO 5 Suppose L is a list of length n, with its elements in sorted order.
# What is the general formula, using n, for the middle element of L? Use this
# formula to print the middle element of names and scores. Hint: Recall that 
# a // b is integer division.

# len(L) // 2   (if there's a .5, it's chopped off, e.g. 5 // 2 = 2)


# TODO 6 After binary search finds the middle element, it checks to see if the
# target value is equal to the middle element, less than the middle element, or
# greater than the middle element. Using the target and list given, write an
# if-elif-else statement that compares the target to the middle element and
# print whether it is equal to it, less than it, or greater than it.
#
# Test it with targets "Charlie", "Allie", and "Zara".
target = "Zara"
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Fred"]
n = len(names)
mid = n // 2
if target == names[mid]:
    print(f'Found it at {mid}')
elif target < names[mid]:
    print(f'{target} might be in left half')
else: # target > names[mid]
    print(f'{target} might be in right half')

# TODO 7 Re-do the previous task, but this time change elif and else parts to
# print the slice of the list where the target might be. Specifically:
# - if target is less than middle element, print the slice from 0 up to, but not 
#   including, mid
# - if target is greater than middle element, print the slice of the list from
#   mid + 1 to to the end
# 
# Test it with targets "Charlie", "Allie", and "Zara".
target = "Zara"
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Fred"]
n = len(names)
mid = n // 2
if target == names[mid]:
    print(f'Found {target} at {mid}')
elif target < names[mid]:
    left = names[:mid]
    print(f'{target} might be in left half: {left}')
else: # target > names[mid]
    right = names[mid+1:]
    print(f'{target} might be in right half: {right}')

#
# a binary search function
#

# TODO 8 Write a function called binary_search that takes two parameters:
# - lst, a sorted list of values to search
# - target, the value to search for
#
# The function should return True if the target is found in the list, and False
# otherwise.
#
# For now, have the function just print "Searching for <target> ..." and return
# False.
def binary_search(lst, target):
    print(f'binary search for {target} in {lst} ...')
    return False

# TODO 9 Now replace the body of the function with the if-elif-else statement
# from above (the one with the slices). Make sure to include mid as a local
# variable at the start. Test it with the list of names and a few different
# targets.
# def binary_search(lst, target):
#     n = len(lst)
#     mid = n // 2
#     if target == lst[mid]:
#         print(f'Found {target} at {mid}')
#         return True
#     elif target < lst[mid]:
#         left = lst[:mid]
#         print(f'{target} might be in left half: {left}')
#         return False # todo: fix this
#     else: # target > lst[mid]
#         right = lst[mid+1:]
#         print(f'{target} might be in right half: {right}')
#         return False # todo: fix this

# names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Fred"]
# print(binary_search(names, "Diana"))
# print(binary_search(names, "Zara"))
# print('empty list', binary_search([], "Zara"))

# TODO 10 We need to handle a special case: when lst is empty, binary search
# should immediately return False. Re-write the function from the previous task
# so that it returns False when lst is empty (and keep everything else the
# same). Test it with the list [] and target "Charlie".

def binary_search(lst, target):
    if lst == []: # base case for recursion
        return False # target not in list

    n = len(lst)
    mid = n // 2
    if target == lst[mid]:
        # print(f'Found {target} at {mid}')
        return True
    elif target < lst[mid]:
        left = lst[:mid]
        # print(f'{target} might be in left half: {left}')
        return binary_search(left, target)
    else: # target > lst[mid]
        right = lst[mid+1:]
        # print(f'{target} might be in right half: {right}')
        return binary_search(right, target)

names = ["Jane", "Mike", "Zeke", "Tina", "Alice", "Bob", "Charlie", "Diana", "Eve", "Fred"]
names.sort()
print(names)
print(binary_search(names, "Diana")) # True
print(binary_search(names, "Zara")) # False
print('empty list', binary_search([], "Zara")) # False


# TODO 11 Copy the function in the previous task and modify it so that it turns
# True if the target is found (remove the print statement that was there
# before). Keep the rest the same. Test it with the target "Charlie" and the
# list ["Alice", "Bob", "Charlie", "Diana", "Eve"]. It should return 2.


# TODO 12 Now we want to replace the other two print statements. Replace them
# with statements of the form "return binary_search(slice, target)", where slice
# is the left or right slice of the list. Test it with the list ["Alice", "Bob",
# "Charlie", "Diana", "Eve"] and targets "Alice", "Charlie", and "Diana".


#
# A test program
#

# TODO 13 Write a test program for binary_search. The program should read a word
# typed by the user, search for it in a sorted list of names, and print whether
# the word was found or not. If the user types 'done', print 'bye bye!' and stop
# the program.
#
# For example:
#
#   --> Alice 
#   found it!
#   --> Zara 
#   NOT found
#   --> Charlie 
#   found it!
#   --> done 
#   bye bye!
#
# Here is pseudocode for the program:
# - set names to ["Alice", "Bob", "Charlie", "Diana", "Eve"] 
# - using input, read a word from the user
# - while the word read from the user is not "done", do the following:
#   - call binary_search to search for the word in names
#   - if the word is found, print "<word> found"
#   - otherwise, print "<word> NOT found"
#   - read a new word from the user
# - print "bye bye!"

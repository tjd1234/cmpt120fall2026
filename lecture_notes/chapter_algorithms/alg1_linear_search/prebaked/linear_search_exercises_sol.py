# linear_search_exercises_sol.py

# TODO 1 Create a new variable called names initialized to this list of strings:
# "Eve", "Diana", "Charlie", "Alice", "Bob". Print it to make sure it's correct.
names = ["Eve", "Diana", "Charlie", "Alice", "Bob"]
print(names)

# TODO 2 Print the length of the names using the len() function.
print(len(names))

# TODO 3 Print the first and last names.
print(names[0])
print(names[-1])

#
# If-statements
#

# TODO 4 Write an if-statement that checks if the string "Alice" is equal to
# target. If it is, print "Found it!". Otherwise, print "Not a match." Test it
# by setting target to first "Alice" and then "Zara".
target = "Alice"
if target == "Alice":
    print("Found it!")
else:
    print("Not a match.")


# TODO 5 Write an if-statement that checks if target appears anywhere in the
# names list using the in operator. Print appropriate messages if is found or
# not found.
if target in names:
    print(f"{target} is in the list.")
else:
    print(f"{target} is not in the list.")

#
# loops
#

# TODO 6 Write a for-loop that prints every element in names, one per line.
for n in names:
    print(n)

# TODO 7 Write a for-loop that prints every element in names along with its
# index. Use the range() and len() functions in the loop. The first line should
# look like: 0 Alice
for i in range(len(names)):
    print(i, names[i])


# TODO 8 Re-do the previous task using the built-in enumerate() function instead
# of range(len(...)). The output should be identical.
for i, n in enumerate(names):
    print(i, n)

# TODO 9 Write a for-loop that goes through all the names and prints the name
# only if it is equal to target.
for n in names:
    if n == target:
        print(n)

#
# building linear search
#

# TODO 10 Re-do the previous task so that it prints the index of where in the
# list the target is found, e.g. if the target is "Charlie", it should print
# "Found Charlie at index 2". Outside the loop at the end print 'done'.
# Test it with the target "Charlie", and then "Zara".
names = ["Eve", "Diana", "Charlie", "Alice", "Bob"]
target = "Charlie"
for i in range(len(names)):
    if names[i] == target:
        print(f"Found {target} at index {i}")
print('done')


# TODO 11 Create a variable called found_index and initialize it to -1. Re-do
# the previous task using but instead of printing the index of where the target
# is found, set found_index to be that index. Then at the end instead of
# printing "done" print "Found <target> at index <found_index>." Test it with the
# target "Charlie", and then "Zara".
names = ["Eve", "Diana", "Charlie", "Alice", "Bob"]
target = "Charlie"
found_index = -1
for i in range(len(names)):
    if names[i] == target:
        found_index = i
print(f"Found {target} at index {found_index}")


#
# functions
#

# TODO 12 Write a function called linear_search that takes two parameters:
#
# - lst, a list of values to search
# - target, the value to search for
#
# The function should return an int representing the index of where the target
# was found, or -1 if the target was not anywhere in the list.
#
# For now, have the function just print "Searching for <target> in <lst> ..." and
# then return -1.
def linear_search(lst, target):
    print(f"Searching for {target} in {lst} ...")
    return -1

# TODO 13 Now remove the print statement and add a loop that searches for target
# in lst. Create a local variable called found_index (initialized to -1) to
# store the index. At the end of the function, return found_index. Test it by
# searching for "Charlie" and then "Zara".
def linear_search(lst, target):
    found_index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            found_index = i
    return found_index

names = ["Eve", "Diana", "Charlie", "Alice", "Bob"]
print(linear_search(names, "Charlie")) # 2
print(linear_search(names, "Zara")) # -1

# TODO 14 If you created the linear_search function as described, then after it
# finds the target it keeps searching. Modify the function so that it returns
# immediately after the target is found. Test it by searching for "Charlie" and
# then "Zara". Hint: It's possible to now get rid of the found_index variable!
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # found target at index i, return immediately
    return -1 # target not found, return -1

names = ["Eve", "Diana", "Charlie", "Alice", "Bob"]
print(linear_search(names, "Charlie")) # 2
print(linear_search(names, "Zara")) # -1

#
# a test program
#

# TODO 15 Now lets write a little program to test linear_search. We want the
# program to read words from the user, search for them in the list of names, and
# then print a message saying whether the word was found or not. If the user
# types 'done', the program should say 'bye bye!' and exit. 
# 
# For example:
# 
#   --> Alice 
#   found at index 3 
#   --> Zara
#   not in the list
#   --> Charlie
#   found at index 2
#   --> done 
#   bye bye!
#
# Here is pseudocode for the program:
# - set names to ["Eve", "Diana", "Charlie", "Alice", "Bob"] 
# - using input, read a word from the user
# - while the word read from the user is not "done", do the following:
#   - call linear_search to search for the word in names
#   - if the word is not found, print "<word> not in the list"
#   - otherwise, print "<word> found at index <index>"
#   - read a new word from the user
# - print "bye bye!"

# names = ["Eve", "Diana", "Charlie", "Alice", "Bob"]
# word = input("--> ")
# while word != "done":
#     index = linear_search(names, word)
#     if index == -1:
#         print(f"{word} not in the list")
#     else:
#         print(f"{word} found at index {index}")
#     word = input("--> ")
# print("bye bye!")


#
# other data types and duplicates
#

# TODO 16 Does linear_search work with other data types? Create a list called
# scores containing the integers: 42, 17, 95, 3, 67, 95, 8. Then re-run the test
# program from the previous task using the scores list instead of names. Does it
# work?

# Yes, linear_search should worth with a list of ints, or any data type for
# which Python's == operator is defined.


# TODO 17 Notice that 95 appears twice in scores (at index 2 and index 5). Call
# linear_search to search for 95 in scores and print the result. Which index
# does it return? Why does linear search behave this way? Explain your answer like
# are speaking to a 5 year old.
scores = [42, 17, 95, 3, 67, 95, 8]
index = linear_search(scores, 95)
print(f"95 found at index {index}")

# The index returned is 2. This is because linear_search searches from left to
# right and returns returns immediately when it finds the target value. So if a
# value (like 95) occurs more than once in the list, the first index of that
# value is returned.

#
# counting and collecting
#

# TODO 18 Write a function called count_occurrences that takes a list and a
# target, and returns how many times the target appears in the list. Use a
# for-loop and a counter variable, and do NOT list.count(). Test it on a few 
# different lists and targets to make sure it works.
def count_occurrences(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

scores = [42, 17, 95, 3, 67, 95, 8]
print(count_occurrences(scores, 95)) # 2
print(count_occurrences(scores, 100)) # 0
print(count_occurrences(scores, 17)) 


# TODO 19 Now write a function call find_all_indices(lst, target) that returns a
# list of every index in lst where target appears. If target is not found at
# all, return an empty list. For example, if scores is [42, 17, 95, 3, 67, 95,
# 8] and target is 95, it should return [2, 5]. If target is 10, then [] is
# returned. Test is with at those values and a couple more.
def find_all_indices(lst, target):
    indices = []
    for i in range(len(lst)):
        if lst[i] == target:
            indices.append(i)
    return indices

scores = [42, 17, 95, 3, 67, 95, 8]
print(find_all_indices(scores, 95)) # [2, 5]
print(find_all_indices(scores, 100)) # []
print(find_all_indices(scores, 17)) # [1]

#
# finding the max
#

# TODO 20 Write a function called get_max(lst) that returns the largest value in
# the lst. Use a for-loop and a variable to keep track of the largest value seen
# so far. Test it on a few different lists to make sure it works, including:
# 
# - the empty list
# - a list of ints (it should return the largest int)
# - a list of strings (it should return the alphabetically last string)

def get_max(lst):
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value

scores = [42, 17, 95, 3, 67, 95, 8]
print(get_max([42, 17, 95, 3, 67, 95, 8])) # 95

names = ["Eve", "Diana", "Charlie", "Alice", "Bob"]
print(get_max(names)) # "Eve"

empty = []
print(get_max(empty)) # error!


# TODO 21 Write a function called longest_string(lst) that returns the longest
# string in the lst. For example, if lst is ["Eve", "Diana", "Charlie", "Alice",
# "Bob"], it should return "Charlie". If lst is empty, return the empty string.

def longest_string(lst):
    longest = ""
    for item in lst:
        if len(item) > len(longest):
            longest = item
    return longest

names = ["Eve", "Diana", "Charlie", "Alice", "Bob"]
empty = []
print(longest_string(names)) # "Charlie"
print(longest_string(empty)) # ""

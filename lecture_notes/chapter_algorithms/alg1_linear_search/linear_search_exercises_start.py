# linear_search_exercises_start.py

# TODO 1 Create a new variable called names initialized to this list of strings:
# "Eve", "Diana", "Charlie", "Alice", "Bob". Print it to make sure it's correct.

# TODO 2 Print the length of the names using the len() function.


# TODO 3 Print the first and last names. Do it in two different ways: one way
# using non-negative indices and one way using negative indices. Do it so it
# works with any list of names.


#
# If-statements
#

# TODO 4 Add new variable called target and initialize it to the empty string.
# Write an if-statement that checks if the string "Alice" is equal to target. If
# it is, print "Found it!". Otherwise, print "Not a match." Test it by setting
# target to first "Alice" and then "Zara".


# TODO 5 Re-do the previous task using so it does the same thing, but use "not
# in" instead of "in".

#
# loops
#

# TODO 6 Write a for-loop that prints every element in names, one per line.


# TODO 7 Write a for-loop that prints every element in names along with its
# index. Use the range() and len() functions in the loop. The first line should
# look like: 0 Alice


# TODO 8 Re-do the previous task using the built-in enumerate() function instead
# of range(len(...)). The output should be identical.


# TODO 9 Write a for-loop that goes through all the names and prints a name only
# if it is equal to target.


#
# building linear search
#

# TODO 10 Re-do the previous task so that it prints the index of where in the
# list the target is found. For example, if the target is "Charlie", it should
# print "Found Charlie at index 2". Outside the loop at the end print 'done'.
# Test it with the target "Charlie", and then "Zara".


# TODO 11 Create a variable called found_index and initialize it to -1. Re-do
# the previous task but instead of printing the index of where the target is
# found, set found_index to be that index. Then at the end instead of printing
# "done" print "Found <target> at index <found_index>." Test it with the target
# "Charlie", and then "Zara".


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


# TODO 13 Now remove the print statement from linear_search and add a loop that
# searches for target in lst. Create a local variable called found_index
# (initialized to -1) to store the index. At the end of the function, return
# found_index. Test it by searching for "Charlie" and then "Zara".


# TODO 14 If you created the linear_search function as described, then after it
# finds the target it keeps searching. Modify the function so that it returns
# immediately after the target is found. Test it by searching for "Charlie" and
# then "Zara". Hint: It's possible to now get rid of the found_index variable!

#
# a test program
#

# TODO 15 Now lets write a little program to test linear_search. We want the
# program to read words from the user, search for them in the list of names, and
# then print a message saying whether the word was found or not. When the user
# types 'done', the program should say 'bye bye!' and exit. 
# 
# Here's a sample run:
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


#
# other data types and duplicates
#

# TODO 16 Does linear_search work with other data types? Create a list called
# scores containing the integers: 42, 17, 95, 3, 67, 95, 8. Then re-run the test
# program from the previous task using the scores list instead of names. Does it
# work?


# TODO 17 Notice that 95 appears twice in scores (at index 2 and index 5). Call
# linear_search to search for 95 in scores and print the result. Which index
# does it return? Why does linear search return that one and not the other?

#
# counting and collecting
#

# TODO 18 Write a function called count_occurrences that takes a list and a
# target as input, and returns how many times the target appears in the list.
# Use a for-loop and a counter variable, and do NOT use list.count(). Test it on
# a few different lists and targets to make sure it works.


# TODO 19 Now write a function call find_all_indices(lst, target) that returns a
# list of every index in lst where target appears. If target is not found at
# all, return an empty list. For example, if scores is [42, 17, 95, 3, 67, 95,
# 8] and target is 95, it should return [2, 5]. If target is 10, then [] is
# returned. Test it with at those values and a couple more.

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


# TODO 21 Write a function called longest_string(lst) that returns the longest
# string in the lst. For example, if lst is ["Eve", "Diana", "Charlie", "Alice",
# "Bob"], it should return "Charlie". If lst is empty, return the empty string.

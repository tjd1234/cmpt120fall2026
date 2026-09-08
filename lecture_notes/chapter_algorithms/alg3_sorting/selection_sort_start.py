# selection_sort_start.py

#
# Selection Sort
#
# Selection sort is an algorithm that re-arranges the elements of a list into
# sorted order. If the list has numbers, then the numbers end up ordered from
# smallest to largest. If the list has strings, then the strings end up in
# alphabetical order.
#
# The idea for how selection sort works is quite intuitive. We'll use two lists:
# a list called unsorted containing the numbers we want to sort, and a second
# list called sorted that starts out empty. Selection sort works like this:
# remove the smallest element from the unsorted list, and append it to the end
# of the sorted list. Keep doing this until unsorted is empty.
# 


# TODO 1 Implement the selection sort algorithm as described above. Name the
# function selection_sort1. It takes a list as input (call it unsorted), and
# returns a new list that is the sorted version of the input list. Hint: for
# this first version it's okay to modify the input list.
# 
# Check it using this code:
#
# scores = [85, 90, 78, 92, 88]
# print('scores before:', scores)
# sorted_scores = selection_sort1(scores)
# print('sorted_scores:', sorted_scores)
# print(' scores after:', scores)


# TODO 2 If you implemented selection_sort1 above as described above, then the
# input list ends up empty at the end (because# remove has been called on all
# its elements). 
# 
# It's usually bad to trash an input list like this --- maybe you want to keep a
# copy of the original list.
#
# So, write a new function called selection_sort2 that works the same as
# selection_sort1, but selection_sort2 does not modify the original input list.
#
# Check it with the same code, but make sure the original list is not modified.
#

# TODO 3 Our version of selection sort is designed to be simple and easy to
# understand. But it is not as efficient as it could be. We can speed it up by
# doing the sorting in place, i.e. without making a second list. The idea is to
# keep the sorted and unsorted lists inside the original list:
#
#        +-------------------+----------------+
#    lst |      sorted       |    unsorted    |
#        +-------------------+----------------+
#
# Using this approach, selection sort finds the min element in the unsorted
# slice, and then swaps it with the first element of the unsorted slice. This is
# the same as removing it and appending it to the sorted part, but faster.
#
# Even with this (and other) improvements, selection sort is still slow.
# Fundamentally, it does more work than necessary. So here we just give a more
# efficient in-place version instead of working it out in detail.

def selection_sort3_in_place(lst):
    for i in range(len(lst)):
        # 1. Slice the unsorted part: lst[i:]
        # 2. Find the index of the minimum value within that slice
        # 3. Add i to get the true index in the original list
        min_idx = lst[i:].index(min(lst[i:])) + i
        
        # 4. Swap the found minimum with the first element of the unsorted part
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

import sortcheck
sortcheck.test(selection_sort3_in_place)

scores = [85, 90, 78, 92, 88]
print('scores before:', scores)
sorted_scores = selection_sort3_in_place(scores)
print('sorted_scores:', sorted_scores)
print(' scores after:', scores)

# TODO 4 How fast is our version of selection sort? To figure this out, lets
# write some code that runs an experiment. Create random lists of numbers of
# sizes n=1000, 2000, ..., 10000 and sort each list. Time how long the sorting
# takes, and then plot the results.
#
# Import these libraries to help with the experiment:
# - import random to get the shuffle function to make random lists
# - import time to get the start and end times of the sorting
#
# Save the results by writing them to a file. Use .csv (comma-separated values)
# format to make it easy to import into a spreadsheet. Once inside a
# spreadsheet, plot the results as a line graph (it should be a parabola).
# 

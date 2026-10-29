# list_functions_start.py

#
# These questions ask you to re-implement some built-in list functions (except
# the last one, which is not a built-in list function).
#
# Do NOT use any built-in list functions your code or other advanced features
# (like list comprehensions)! The idea is to see how they can be implemented
# using only slicing and basic Python features.
#
# Each function has a simple test function that you can use to check if your
# code works. Be careful: it is possible for your code to pass the test function
# but still not work correctly in all cases!
#
# The goal here is simplicity and brevity, not efficiency (the built-in list
# functions are optimized for speed).
# 
# After you've written a function you can re-use it in later questions.
#


# TODO 1 Write a function called my_clear(L) that takes any list L as input and
# returns the empty list. For example:
#
# L = [1, 2, 3]
# new_L = my_clear(L)
# print(new_L) # []
#
# Hint: Can be done in one line.


def my_clear(L):
    pass


def my_clear_test():
    L = [1, 2, 3]
    new_L = my_clear(L)
    print(new_L)  # []
    assert new_L == []
    assert L == [1, 2, 3]
    L = ["a", "b", "c"]

    new_L = my_clear(L)
    print(new_L)  # []
    assert new_L == []
    assert L == ["a", "b", "c"]
    print("my_clear_test passed")


my_clear_test()


# TODO 2 Write a function called my_pop(L) that takes any list L as input and
# returns a copy of L except the last element is removed. For example:
#
# L = [1, 2, 3]
# rest = my_pop(L)
# print(rest) # [1, 2]
# print(L) # [1, 2, 3]
#
# You can assume L is not the empty list.
#
# Hint: Can be done in one line.
def my_pop(L):
    pass


def my_pop_test():
    L = [1, 2, 3]
    rest = my_pop(L)
    print(rest)  # [1, 2]
    print(L)  # [1, 2, 3]
    assert rest == [1, 2]
    assert L == [1, 2, 3]
    print("my_pop_test passed")


my_pop_test()


# TODO 3 Write a function called my_append(L, x) that returns a new list that is
# the same as L, but with x added to the end. For example:
#
# L = [1, 2, 3]
# new_L = my_append(L, 4)
# print(new_L) # [1, 2, 3, 4]
# print(L) # [1, 2, 3]
#
# Hint: Can be done in one line.
def my_append(L, x):
    pass


def my_append_test():
    L = [1, 2, 3]
    new_L = my_append(L, 4)
    print(new_L)  # [1, 2, 3, 4]
    print(L)  # [1, 2, 3]
    assert new_L == [1, 2, 3, 4]
    assert L == [1, 2, 3]
    print("my_append_test passed")


my_append_test()


# TODO 4 Write a function called my_copy(L) that returns a new copy of L. For example:
#
# L = [1, 2, 3]
# new_L = my_copy(L)
# print(new_L) # [1, 2, 3]
# print(L) # [1, 2, 3]
#
# Hint: Can be done in one line.
def my_copy(L):
    pass


def my_copy_test():
    L = [1, 2, 3]
    new_L = my_copy(L)
    L.append(4)
    print(new_L)  # [1, 2, 3]
    assert new_L == [1, 2, 3]
    assert L == [1, 2, 3, 4]
    print("my_copy_test passed")


my_copy_test()


# TODO 5 Write a function called my_reverse(L) that returns a new list that is the reverse of L. For example:
#
# L = [1, 2, 3]
# new_L = my_reverse(L)
# print(new_L) # [3, 2, 1]
# print(L) # [1, 2, 3]
#
# Hint: Can be done in one line.
def my_reverse(L):
    pass


def my_reverse_test():
    L = [1, 2, 3]
    new_L = my_reverse(L)
    print(new_L)  # [3, 2, 1]
    print(L)  # [1, 2, 3]
    assert new_L == [3, 2, 1]
    assert L == [1, 2, 3]
    print("my_reverse_test passed")


my_reverse_test()


# TODO 6 Write a function called my_extend(L, other) that returns a new list
# that is the same as L except all the elements of other are added to the end
# of L. For example:
#
# L = [1, 2, 3]
# other = [4, 5, 6]
# new_L = my_extend(L, other)
# print(new_L) # [1, 2, 3, 4, 5, 6]
# print(L) # [1, 2, 3]
#
# Hint: Can be done in one line.
def my_extend(L, other):
    pass


def my_extend_test():
    L = [1, 2, 3]
    other = [4, 5, 6]
    new_L = my_extend(L, other)
    print(new_L)  # [1, 2, 3, 4, 5, 6]
    print(L)  # [1, 2, 3]
    assert new_L == [1, 2, 3, 4, 5, 6]
    assert L == [1, 2, 3]
    print("my_extend_test passed")


my_extend_test()


# TODO 7 Write a function called my_count(L, x) that returns the number of times
# x appears in L. For example:
#
# L = [1, 2, 3, 2, 1]
# count = my_count(L, 2)
# print(count) # 2
#
def my_count(L, x):
    pass


def my_count_test():
    L = [1, 2, 3, 2, 1]
    count = my_count(L, 2)
    print(count)  # 2
    assert count == 2
    assert L == [1, 2, 3, 2, 1]
    print("my_count_test passed")


my_count_test()


# TODO 8 Write a function called my_index(L, x) that returns the index of the
# first occurrence of x in L. If x is not found, return -1. For example:
#
# print(my_index([1, 2, 3, 2, 1], 2))  # 1
# print(my_index([1, 2, 3, 2, 1], 4))  # -1
#
def my_index(L, x):
    pass


def my_index_test():
    i1 = my_index([1, 2, 3, 2, 1], 2)
    i2 = my_index([1, 2, 3, 2, 1], 4)
    print(i1)  # 1
    print(i2)  # -1
    assert i1 == 1
    assert i2 == -1
    print("my_index_test passed")


my_index_test()


# TODO 9 Write a function called my_remove(L, x) that returns a new list that is
# the same as L except the first occurrence of x is removed. If x is not found,
# return a copy of L. For example:
#
# print(my_remove([1, 2, 3, 2, 1], 2))  # [1, 3, 2, 1]
# print(my_remove([1, 2, 3, 2, 1], 4))  # [1, 2, 3, 2, 1]
#
# Hint: You can use previous functions you've written.
def my_remove(L, x):
    pass


def my_remove_test():
    L1 = my_remove([1, 2, 3, 2, 1], 2)
    L2 = my_remove([1, 2, 3, 2, 1], 4)
    print(L1)  # [1, 3, 2, 1]
    print(L2)  # [1, 2, 3, 2, 1]
    assert L1 == [1, 3, 2, 1]
    assert L2 == [1, 2, 3, 2, 1]
    print("my_remove_test passed")


my_remove_test()

# TODO 10 Write a function called my_remove_all(L, x) that returns a new list
# that is the same as L except all occurrences of x are removed. For example:
#
# print(my_remove_all([1, 2, 3, 2, 1], 2))  # [1, 3, 1]
# print(my_remove_all([1, 2, 3, 2, 1], 4))  # [1, 2, 3, 2, 1]
#
def my_remove_all(L, x):
    pass

def my_remove_all_test():
    L1 = my_remove_all([1, 2, 3, 2, 1], 2)
    L2 = my_remove_all([1, 2, 3, 2, 1], 4)
    print(L1)  # [1, 3, 1]
    print(L2)  # [1, 2, 3, 2, 1]
    assert L1 == [1, 3, 1]
    assert L2 == [1, 2, 3, 2, 1]
    print("my_remove_all_test passed")

my_remove_all_test()

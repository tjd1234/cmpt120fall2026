# q4.py

"""
Write a function called selection_sort(lst) that returns a sorted copy of the
list. Sorted means the following:

- if lst is a list of numbers, then the numbers are arranged from smallest to
  biggest

- if lst is a list of strings, then the strings are arranged in alphabetic order

For example:

```
prices = [2.3, 1.0, 5.5, 10.2, 1.75]
sorted_prices = selection_sort(prices)
print(sorted_prices)  # [1.0, 1.75, 2.3, 5.5, 10.2]

names = ["David", "Charlie", "Alice", "Bob"]
sorted_names = selection_sort(names)
print(sorted_names)  # ['Alice', 'Bob', 'Charlie', 'David']
```

Important: the selection_sort(L) function should NOT modify the list L.

To sort the list L using selection sort, do the following:
- make a new empty list called result
- as long as there are items left in L repeat the following steps:
  - get and remove the smallest element from L
  - append that smallest element to the end of result

"""

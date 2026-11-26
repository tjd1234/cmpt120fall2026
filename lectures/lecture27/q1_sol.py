# q1_sol.py

"""
Write a function called selector_sort_file(fname) that takes the name of a file
as input, and, assuming it has one word per line, sorts the words into
alphabetical order using selection sort, and then prints the time it took to do
the sorting (and how many words were sorted).

To time a piece of a code, do this:

```
import time

start_time = time.time()
# ... do something ...
end_time = time.time()

elapsed_seconds = end_time - start_time

print(f'Time taken: {elapsed_seconds} seconds')
```

Run your function on the files words1000.txt, words5000.txt, ...
words50000.txt, and record the results.

Your program can have this structure:

```
def selection_sort_file(fname):
    # ... code ...

selection_sort_file('words1000.txt')
selection_sort_file('words5000.txt')
selection_sort_file('words10000.txt')
selection_sort_file('words15000.txt')
selection_sort_file('words20000.txt')
selection_sort_file('words25000.txt')
selection_sort_file('words30000.txt')
selection_sort_file('words35000.txt')
selection_sort_file('words40000.txt')
selection_sort_file('words45000.txt')
selection_sort_file('words50000.txt')
```
"""

def selection_sort(lst):
    unsorted = lst[:]  # makes a copy of lst
    result = []
    while len(unsorted) > 0:
        smallest = min(unsorted)
        unsorted.remove(smallest)
        result.append(smallest)
    return result

def selection_sort_file(fname):
    #
    # read the words into a list
    #
    word_file = open(fname, 'r')
    all_words = []
    for line in word_file:
        word = line.strip()
        all_words.append(word)
    word_file.close()

    #
    # sort the words and time it
    #
    import time
    start_time = time.time()
    sorted_words = selection_sort(all_words)
    end_time = time.time()
    elapsed_seconds = end_time - start_time

    #
    # print the result
    #
    print(f'Time taken to sort {fname}: {elapsed_seconds} seconds')

selection_sort_file('words1000.txt')
selection_sort_file('words5000.txt')
selection_sort_file('words10000.txt')
selection_sort_file('words15000.txt')
selection_sort_file('words20000.txt')
selection_sort_file('words25000.txt')
selection_sort_file('words30000.txt')
selection_sort_file('words35000.txt')
selection_sort_file('words40000.txt')
selection_sort_file('words45000.txt')
selection_sort_file('words50000.txt')

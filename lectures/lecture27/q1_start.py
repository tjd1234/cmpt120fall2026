# q1_start.py

"""
Write a function called selection_sort_file(infile_name, outfile_name) that
copies the words from infile_name (one word per line) in sorted order into
outfile_name (one word per line). The function does the following:

- reads the words from infile_name into a list

- sorts the list into alphabetical order using selection sort

- prints the name of the file and the time it took to do the sorting

- copies the list into outfile_name (overwriting it if it already exists)
  
You can time code like this:

```
import time

start_time = time.time()
# ... do something ...
end_time = time.time()

elapsed_seconds = end_time - start_time

print(f'Time taken: {elapsed_seconds} seconds')
```

Run your function on the eleven files unsorted1000.txt, unsorted5000.txt, ...
unsorted50000.txt, and record the results.

"""

def selection_sort(lst):
    unsorted = lst[:]  # makes a copy of lst
    result = []
    while len(unsorted) > 0:
        smallest = min(unsorted)
        unsorted.remove(smallest)
        result.append(smallest)
    return result

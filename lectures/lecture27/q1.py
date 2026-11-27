# q1.py

"""
Write a function called selector_sort_file(infile_name, outfile_name) that
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

Run your function on the ten files unsorted5000.txt, ..., unsorted50000.txt, and
record the results.
"""

def selection_sort(lst):
    unsorted = lst[:]  # makes a copy of lst
    result = []
    while len(unsorted) > 0:
        smallest = min(unsorted)
        unsorted.remove(smallest)
        result.append(smallest)
    return result

def selection_sort_file(infile_name, outfile_name):
    #
    # read the words into a list
    #
    word_file = open(infile_name, 'r')
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
    # copy the sorted words into the file sorted.txt
    #
    sorted_file = open(outfile_name, 'w')
    for word in sorted_words:
        sorted_file.write(word + '\n')
    sorted_file.close()

    #
    # print the result
    #
    print(f'Time to sort {infile_name}: {elapsed_seconds} seconds')
    


selection_sort_file('unsorted5000.txt', 'sorted5000.txt')
selection_sort_file('unsorted10000.txt', 'sorted10000.txt')
selection_sort_file('unsorted15000.txt', 'sorted15000.txt')
selection_sort_file('unsorted20000.txt', 'sorted20000.txt')
selection_sort_file('unsorted25000.txt', 'sorted25000.txt')
selection_sort_file('unsorted30000.txt', 'sorted30000.txt')
selection_sort_file('unsorted35000.txt', 'sorted35000.txt')
selection_sort_file('unsorted40000.txt', 'sorted40000.txt')
selection_sort_file('unsorted45000.txt', 'sorted45000.txt')
selection_sort_file('unsorted50000.txt', 'sorted50000.txt')

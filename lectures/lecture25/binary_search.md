# Binary Search with Boxes

## Part 1: The Binary Search Algorithm

**Binary search** is a *very* efficient search algorithm that can find a target
value in a list of values that is in *sorted* order. Sorted order means that the
values are in ascending order, i.e. from smallest to biggest. For instance, `[1,
4, 7, 10]` is sorted, but `[10, 7, 1, 4]` is not.

Suppose you have 100 boxes numbered from 0 to 99. Each box has a different
numeric value that you can't see until you open the box. We know for sure that
the values are in sorted order, from smallest to biggest. Thus, we can search
for a given target value using binary search.

Binary search uses two index variables, `low` and `high`. Initially, `low` is 0
and `high` is 99. The idea is that *if* the target is a box, then it is in one
of the boxes numbered from `low` to `high`.

The trick of binary search is to check the box in the *middle* of the range of
boxes, i.e. the box at index `mid = (low + high) // 2`. If that has the target,
then you are done. Otherwise, we can discard *half* of the boxes from
consideration:

- If the target is *less than* the value in the middle box, then the target must
  be in a box in the range from `low` to `mid - 1`.

- If the target is *greater than* the value in the middle box, then the target
  must be in a box in the range from `mid + 1` to `high`.

Eventually, this will either find the target, or make the range of boxes empty
(in which case the target is not in any box).

Here is some Python-like pseudocode for binary search:

```
low = smallest box number
high = largest box number
found_index = -1    # -1 means "not found yet"
while still boxes to check and target not found:
    mid = number of the middle box
    value = value in the middle box
    if the target and value are the same
        found_index = mid
    elif the value is less than the target
        low = number of the box to the right of the middle box
    elsif the value is greater than the target
        high = number of the box to the left of the middle box
```

## Part 2: Implementing Binary Search

Implement binary search using [boxes.py](boxes.py) to display the boxes and open
them. Write code that opens the boxes one at a time, starting at box 0, until
you find the target value.

Write code that implements the above algorithm. Highlight the box the target is
in and print its index, or print a message if the target is not in any box.

Start with [binary_search_start.py](binary_search_start.py). It has some code
already written for you --- you only need to write binary search in the middle
of the program. Use these helper functions:

- `boxes.num_boxes()` returns how many boxes there are
- `boxes.open_box(i)` opens box `i` and returns the number inside it

For now, stick to 100 boxes, and with the target guaranteed to be in one of the
boxes.

Don't change any of the given code that sets up the window and displays the
boxes. Just write linear search in the part where the comments say.

### Questions

1. For n=100 boxes, what is the index number of the *first* box that is opened?
   Why that number?

2. For n=100 boxes, what is the smallest number of boxes binary search might
   open?

3. For n=100 boxes, what is the largest number of boxes binary search might
   open?

## Part 3: Fewer Boxes

Test your program with n=10 boxes.

4. For n=10 boxes, what is the index number of the *first* box that is opened?
   Why that number?

5. For n=10 boxes, what is the smallest number of boxes linear search might
   open?

6. For n=10 boxes, what is the largest number of boxes linear search might
   open?

## Part 4: Searching for a Value that is Not in the Boxes

Modify your program to search for the target value -1, which is guaranteed to
not be in any of the boxes.

7. For n=100 boxes, what is the smallest number of boxes linear search might
   open?
   
8. For n=100 boxes, what is the largest number of boxes linear search might
   open?

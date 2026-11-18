# Linear Search with Boxes

## Part 1: The Linear Search Algorithm

Linear search is a simple and very general algorithm that can find a target
value among group of other values.

To understand it, suppose you have 10 boxes, numbered from 0 to 9. Each box
contains a number, and for simplicity we'll assume all the numbers are unique.
How can you determine if the number 5 is one of the boxes? You can answer it
like this:

1. Open box 0. If the number is 5, you're done.
2. Open box 1. If the number is 5, you're done.
3. Open box 2. If the number is 5, you're done.
4. Open box 3. If the number is 5, you're done.
5. Open box 4. If the number is 5, you're done.
6. Open box 5. If the number is 5, you're done.
7. Open box 6. If the number is 5, you're done.
8. Open box 7. If the number is 5, you're done.
9. Open box 8. If the number is 5, you're done.
10. Open box 9. If the number is 5, you're done.

After these 10 steps, you've either found the number 5 in a particular box, or
you've checked all the boxes and so proven the number 5 is not in any box.

Instead of explicitly listing all the steps, we can use a loop to open the
boxes. Here is some pseudocode (i.e. not quite Python code, but close) that does
this:

```
found_index = -1   # -1 means "not found yet" 
i = 0 
while i < 10 and found_index == -1
    if the value in box i is 5
        found_index = i
    i += 1

if found_index == -1
    print("5 is not in any box")
else
    print("Found 5 in box", found_index)
```

## Part 2: Implementing Linear Search

Implement linear search using [boxes.py](boxes.py) to display the boxes and open
them. Write code that opens the boxes one at a time, starting at box 0, until
you find the target value.

Start with [linear_search_start.py](linear_search_start.py). It has some code
already written for you --- you only need to write linear search in the middle
of the program. Use these helper functions:

- `boxes.num_boxes()` returns how many boxes there are
- `boxes.open_box(i)` opens box `i` and returns the number inside it

For now, stick to 10 boxes, and with the target guaranteed to be in one of the
boxes.

Don't change any of the given code that sets up the window and displays the
boxes. Just write linear search in the part where the comments say. 

1. For n=10 boxes, what is the smallest, largest, and average number of boxes
   linear search might open?

## Part 3: More Boxes

Test your program with n=100 boxes. You can use `set_speed(speed)` make it go
faster: `speed` 1 is the slowest, and `speed` 10 is the fastest.

2. For n=100 boxes, what is the smallest, largest, and average number of boxes
   linear search might open?

## Part 4: Searching for a Value that is Not in the Boxes

Modify your program to search for the target value -1, which is guaranteed to
not be in any of the boxes.

3. For n=100 boxes, what is the smallest, largest, and average number of boxes
   linear search might open?

4. Suppose you are using linear search to search n boxes, and there is a 50%
    chance that the target value is in one of the boxes. What is the average
    number of boxes you would expect linear search to open?

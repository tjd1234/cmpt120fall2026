# q4_sol.py

"""
A race between linear search and binary search!

There are 100 boxes with their numbers in sorted order. Search for the same
target twice:

1. First use linear search (as in q2). When it finishes, save the number of
   boxes it opened in a variable called linear_count.

2. Then wait for the Next button to be clicked (so there is time to look at
   what linear search did), close all the boxes, and use binary search (as
   in q3). When it finishes, save the number of boxes it opened in a variable
   called binary_count.

Finally, print both counts.

These functions will help:

- boxes.num_opened() returns the number of boxes opened so far
- boxes.close_all() closes all the boxes and sets the counter back to 0
- boxes.show_title(title) shows a title at the top of the window
- boxes.wait_for_button("Next") shows a Next button and waits for a click

Sample Run (your numbers will be different)

```
Linear search opened 75 boxes
Binary search opened 4 boxes
```

Run your program a few times. Does binary search always win?
"""
import boxes

boxes.setup(100, sorted=True)
boxes.set_speed(10)             # 100 boxes is a lot, so open them quickly
target = boxes.random_value()   # a number that is in one of the boxes
boxes.show_target(target)

boxes.show_title("Linear search")
boxes.wait_for_start()

# Linear search
found_index = -1    # -1 means "not found yet"
i = 0
while i < boxes.num_boxes() and found_index == -1:
    value = boxes.open_box(i)
    if value == target:
        found_index = i
    i += 1
boxes.highlight_box(found_index)
linear_count = boxes.num_opened()

boxes.wait_for_button("Next")   # pause so the linear search result can be seen
boxes.close_all()
boxes.show_title("Binary search")

# Binary search
low = 0
high = boxes.num_boxes() - 1
found_index = -1
while low <= high and found_index == -1:
    mid = (low + high) // 2
    value = boxes.open_box(mid)
    if value == target:
        found_index = mid
    elif value < target:
        low = mid + 1     # target must be to the right of box mid
    else:
        high = mid - 1    # target must be to the left of box mid
boxes.highlight_box(found_index)
binary_count = boxes.num_opened()

print("Linear search opened", linear_count, "boxes")
print("Binary search opened", binary_count, "boxes")

# Binary search doesn't always win. If the target is in one of the first few
# boxes, linear search finds it in fewer opens. But linear search can need as
# many as 100 opens, while binary search never needs more than 7.

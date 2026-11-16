# q1_sol.py

"""
Each box in the window hides a number. The only way to find out what is in a
box is to open it by calling boxes.open_box(i), which returns the number
inside box i. The first box is box 0.

Write a program that finds which box the target number is in using *linear
search*: open the boxes one at a time, starting at box 0, until you find the
target. Then stop opening boxes, highlight the box the target is in, and print
its index.

These functions will help:

- boxes.open_box(i) opens box i and returns the number inside it
- boxes.num_boxes() returns how many boxes there are
- boxes.highlight_box(i) colours box i green

Sample Run (your numbers will be different)

```
Found 64 in box 6
```

When your program is working, run it a few times and watch the "Boxes opened"
counter. What is the smallest it could ever be? What is the largest?
"""
import boxes

boxes.setup(10)
boxes.show_title("Linear search")
target = boxes.random_value()   # a number that is in one of the boxes
boxes.show_target(target)
boxes.wait_for_start()

found_index = -1    # -1 means "not found yet"
i = 0
while i < boxes.num_boxes() and found_index == -1:
    value = boxes.open_box(i)
    if value == target:
        found_index = i
    i += 1

boxes.highlight_box(found_index)
print("Found", target, "in box", found_index)

# The smallest the counter could be is 1 (the target is in box 0). The largest
# is 10 (the target is in the last box).

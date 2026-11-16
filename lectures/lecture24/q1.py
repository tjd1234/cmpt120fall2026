# q1.py

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
target = boxes.pick_target_value()   # a number that is in one of the boxes
boxes.show_target(target)
boxes.wait_for_start()

# TODO: open the boxes one at a time, starting at box 0, until you find
# target. Highlight the box it is in, and print its index.


boxes.done()   # keep the window open and show the Restart button

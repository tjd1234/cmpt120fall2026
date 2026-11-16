# q2.py

"""
What happens if the target is not in any of the boxes?

The numbers hidden in the boxes are always 1 or bigger, so 0 is never in a
box. The program below is the linear search from q1, but with the target
changed to 0. Run it and see what goes wrong.

Fix the program so that it works whether or not the target is in a box:

- if the target is in a box, highlight the box and print its index (as before)
- if the target is not in any box, print a message saying so

Sample Run (target is 0)

```
0 is not in any box
```

Sample Run (target is in a box; your numbers will be different)

```
Found 64 in box 6
```

Test your program both ways: with target = 0, and with
target = boxes.pick_target_value().

How many boxes does linear search open when the target is not there?
"""
import boxes

boxes.setup(10)
boxes.show_title("Linear search")
target = 0   # 0 is never in a box
boxes.show_target(target)
boxes.wait_for_start()

found_index = -1    # -1 means "not found yet"
i = 0
while i < boxes.num_boxes() and found_index == -1:
    value = boxes.open_box(i)
    if value == target:
        found_index = i
    i += 1

# TODO: fix the two lines below so the program also works when the target is
# not in any box
boxes.highlight_box(found_index)
print("Found", target, "in box", found_index)

boxes.done()   # keep the window open and show the Restart button

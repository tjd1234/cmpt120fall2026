# q3.py

"""
There are 100 boxes, and the numbers in them are in *sorted order*, from
smallest (box 0) to largest (box 99).

Write a program that finds which box the target number is in using *binary
search*. The idea of binary search is as follows:

- use two variables, low and high, to keep track of the range of boxes where the
  target could be

- initially, the target could be in any of the 100 boxes, so start with low = 0
  and high = boxes.num_boxes() - 1

- open the box in the middle of low and high, and check if it contains the
  target; there are three possibilities: 
  
  1. the target is in the box, you're done
  
  2. the target is less than the number in the box, so it must be in a box to
     the left of the middle box; so change high to the box before the middle

  3. the target is greater than the number in the box, so it must be in a box to
     the *right* of the current box, so change low to the box after the current
     box

- if after doing the above, there are still boxes left that the target could be
  in, then repeat the process with the new range of boxes

- if instead there are no boxes left that the target could be in, then the
  target is not in any box. and you are done

Write code that implements the above algorithm. Highlight the box the target is
in and print its index, or print a message if the target is not in any box.

Sample Run (your numbers will be different)

```
Found 780 in box 74
```

Sample Run (target is 0)

```
0 is not in any box
```

Watch the "Boxes opened" counter. What is the largest it ever gets?
"""
import boxes

boxes.setup(100, sorted=True)
boxes.show_title("Binary search")
target = boxes.pick_target_value()   # a number that is in one of the boxes
boxes.show_target(target)
boxes.wait_for_start()

low = 0
high = boxes.num_boxes() - 1
found_index = -1    # -1 means "not found yet"

# TODO: write a while-loop that does the binary search. Each time through the
# loop it should:
#
# - set mid to the index of the box in the middle of low and high; use
#   (low + high) // 2
# - open box mid
# - compare the number in that box to target, and then either set
#   found_index, or change low, or change high


if found_index == -1:
    print(target, "is not in any box")
else:
    boxes.highlight_box(found_index)
    print("Found", target, "in box", found_index)

boxes.done()   # keep the window open and show the Restart button

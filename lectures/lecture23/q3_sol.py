# q3_sol.py

"""
There are 100 boxes, and the numbers in them are in *sorted order*, from
smallest (box 0) to largest (box 99).

Write a program that finds which box the target number is in using *binary
search*. The idea of binary search is as follows:

- use two variables, low and high, to keep track of the range of boxes where the
  target could be

- initially, the target could be in any of the 100 boxes, so start with low = 0
  and high = 99

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
"""
import boxes

boxes.setup(100, sorted=True)
boxes.show_title("Binary search")
target = boxes.random_value()   # a number that is in one of the boxes
boxes.show_target(target)
boxes.wait_for_start()

low = 0
high = boxes.num_boxes() - 1
found_index = -1    # -1 means "not found yet"
while low <= high and found_index == -1:
    mid = (low + high) // 2
    value = boxes.open_box(mid)
    if value == target:
        found_index = mid
    elif value < target:
        low = mid + 1     # target must be to the right of box mid
    else:
        high = mid - 1    # target must be to the left of box mid

if found_index == -1:
    print(target, "is not in any box")
else:
    boxes.highlight_box(found_index)
    print("Found", target, "in box", found_index)
    print("Binary search opened", boxes.num_opened(), "boxes")

# With 100 boxes, binary search never opens more than 7 boxes.

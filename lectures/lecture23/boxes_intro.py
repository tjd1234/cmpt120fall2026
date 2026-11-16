"""
A first look at the boxes module: how to make the boxes, give the window a
title, open boxes, and highlight one.
"""

import boxes

# make a window with 5 closed boxes; each box hides a number
boxes.setup(5)

# Put a title at the top of the window
boxes.show_title("Meet the boxes")

# show a a start button; wait for it to be clicked
boxes.wait_for_start()

# open box 0 (the first box) and get the number inside it
value = boxes.open_box(0)
print("Box 0 holds", value)

# open box 3
value = boxes.open_box(3)
print("Box 3 holds", value)

# colour box 3 green
boxes.highlight_box(3)

# print results
print("Number of boxes:", boxes.num_boxes())
print("Boxes opened:", boxes.num_opened())

# When the program ends, the window stays open and a Restart button appears.
# Click Restart to run the program again, or close the window to finish.

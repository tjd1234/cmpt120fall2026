"""
Demo of the boxes module: linear search.

Picks a target number that is hidden in one of the boxes, then opens the
boxes one at a time from left to right until the target is found.
"""

import boxes

boxes.setup(10)
boxes.show_title("Linear search")
target = boxes.pick_target_value()
boxes.show_target(target)
boxes.wait_for_start()
print("Searching for", target)

found_index = -1
i = 0
while i < boxes.num_boxes() and found_index == -1:
    value = boxes.open_box(i)
    if value == target:
        found_index = i
    i += 1

boxes.highlight_box(found_index)
print("Found", target, "in box", found_index)
print("Boxes opened:", boxes.num_opened())

boxes.done()   # keep the window open and show the Restart button

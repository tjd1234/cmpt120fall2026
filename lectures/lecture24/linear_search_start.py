# linear_search_start.py

"""
See linear_search.md.
"""

import boxes

#
# Set the number of boxes and give the window a title
#
boxes.setup(10)
boxes.show_title("Linear search")


#
# target is the value being searched for
#
# boxes.pick_target_value() randomly chooses a value from one of the boxes (it
# is guaranteed to be in one of the boxes)
#
target = boxes.pick_target_value()

#
# display the target value so the user can see what is being search for
#
boxes.show_target(target)

#
# wait for the use to click the Start button
#
boxes.wait_for_start()

#
# linear search algorithm
#

# ... your code here ..


#
# when it's done, visually highlight the box containing the target value
#
boxes.highlight_box(found_index)
print(f'Found {target} in box {found_index}')

#
# keep the window open and show the Restart button
#
boxes.done()   # keep the window open and show the Restart button

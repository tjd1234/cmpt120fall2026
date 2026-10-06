"""
Like demo.py, but the second hand moves smoothly instead of jumping every second.
Updates the clock often and sets the second-hand angle from elapsed time.
"""

import time
import clock

clock.set_window_position(1480, 100)
clock.set_show_minute_ticks(True)
clock.set_show_quarter_ticks(True)
clock.draw_clock()

start = time.time()
while True:
    elapsed = time.time() - start
    seconds = elapsed % 60  # 0..59 with fractional part
    clock.set_second_hand_angle(seconds * 6)  # 6° per second
    time.sleep(0.05)  # update every 50 ms for smooth motion

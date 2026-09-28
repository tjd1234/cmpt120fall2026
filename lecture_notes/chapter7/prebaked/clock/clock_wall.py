"""
Demonstration of the clock module.
Shows a live clock with hands that move every second to the current time.
Uses a simple loop to update the second hand (and minute/hour) each second.
"""

import time
import clock

clock.set_window_position(1480, 100)
clock.set_show_minute_ticks(True)
clock.set_show_quarter_ticks(True)
clock.set_show_numbers(True)
clock.draw_clock()

while True:
    #
    # get the current time
    # 
    now = time.localtime()
    #
    # set each hand to the current time
    #
    clock.set_second_hand_angle(now.tm_sec * 6)
    clock.set_minute_hand_angle(now.tm_min * 6 + now.tm_sec * 0.1)
    clock.set_hour_hand_angle(now.tm_hour % 12 * 30 + now.tm_min * 0.5)
    #
    # wait for 1 second
    #
    time.sleep(1)

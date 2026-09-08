# demo_second_hand.py

import time
import clock

clock.set_window_position(1480, 100)
clock.set_show_minute_ticks(True)
clock.set_show_quarter_ticks(True)
clock.draw_clock()

angle = 0
while True:
    clock.set_second_hand_angle(angle)
    angle = angle + 6 # 6 is 360 // 60
    if angle >= 360:
        angle = 0
    time.sleep(1)

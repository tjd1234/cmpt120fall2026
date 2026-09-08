# curtain_sol.py

import stage
import time

stage.curtain_up()  # Curtain moves slowly up until fully open

while stage.get_height() < 1.0:
    stage.update()  # Let the animation run

time.sleep(1)
stage.curtain_down()  # Curtain moves slowly down until fully closed

while stage.get_height() > 0.0:
    stage.update()  # Let the animation run

stage.keep_window_open()

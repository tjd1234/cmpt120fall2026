# Clock Module

A Python module that draws a clock face using turtle graphics. The clock has a
second hand, a minute hand, and hour hand that can each be set to a specific
angle. Tick marks and numbers can be drawn at various positions around the clock
face, or hidden entirely.

## Functions

### Setting hand angles

- **`set_second_hand_angle(angle)`**  
- **`set_minute_hand_angle(angle)`**  
- **`set_hour_hand_angle(angle)`**  

Each setter takes a number for the angle of the hand. All angles are in
**degrees**:

- **0°** = 12 o’clock (straight up)
- **90°** = 3 o’clock
- **180°** = 6 o’clock
- **270°** = 9 o’clock

Angles increase **clockwise**. One full rotation is 360°.

If the clock window is already open (after `draw_clock()` has been called), the
display updates immediately. You can call the setters any number of times for
live-updating.

- **`set_window_position(startx, starty)`**  
  Sets the position of the window on the screen when the clock is drawn.
  `startx` is the horizontal position in pixels from the left edge of the
  screen; `starty` is the vertical position in pixels from the top edge. Pass
  `None` for either argument to leave that axis at the default (centered).

- **`set_show_minute_ticks(show)`**  
  Turn the 60 minute tick marks on/off. When on, every minute position has a
  tick; positions on the hour (1, 2, 4, 5, …) are drawn slightly longer. Pass
  `True` to show them, `False` to hide. Default is on.

- **`set_show_quarter_ticks(show)`**  
  Turn the quarter-hour tick marks (12, 3, 6, 9) on/off. These are the thickest,
  longest ticks. Pass `True` to show them, `False` to hide. Default is on.

- **`set_show_numbers(show)`**  
  Turn the hour numbers (1–12) around the edge of the clock on/off. Pass `True`
  to show them, `False` to hide. Default is on.

### Drawing

- **`draw_clock()`**  
  Draws the clock face and the three hands at their current angles. The second
  hand is red; the minute and hour hands are black, with the hour hand thicker.
  Returns immediately; you must call `turtle.done()` afterward to keep the
  window open and responsive. Once the clock is drawn, any call to a hand or
  visibility setter updates the display instantly.

## Typical usage

1. Set the angles for each hand (optional before drawing).
2. Call `draw_clock()` once to display the clock.
3. Call `turtle.done()` to keep the window open. After that, calling any hand
   setter will redraw the clock with the new angles.

Example (static 10:15:30):

```python
import turtle
import clock

clock.set_hour_hand_angle(300)    # 10 * 30°
clock.set_minute_hand_angle(90)   # 15 * 6°
clock.set_second_hand_angle(180)  # 30 * 6°
clock.draw_clock()
turtle.done()
```

Example (live clock showing current time, updating every second):

```python
import time
import turtle
import clock

def tick():
    now = time.localtime()
    clock.set_second_hand_angle(now.tm_sec * 6)
    clock.set_minute_hand_angle(now.tm_min * 6 + now.tm_sec * 0.1)
    clock.set_hour_hand_angle(now.tm_hour % 12 * 30 + now.tm_min * 0.5)
    turtle.ontimer(tick, 1000)

clock.draw_clock()
tick()
turtle.done()
```

## Challenge

Make the clock show the current time, updating every second.

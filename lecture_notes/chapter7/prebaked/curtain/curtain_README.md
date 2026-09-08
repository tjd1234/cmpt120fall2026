# Stage with curtain

A Python module that shows a stage with a curtain. It has these functions:

- `curtain_up()` makes the current go up, stopping when it reaches the to or
  `curtain_down()` is called.

- `curtain_down()` works the same way, but goes down. 

- `get_height()` returns the current curtain height: **0.0** = fully closed,
  **1.0** = fully open. You can call this anytime to see where the curtain is.

- `update()` processes pending events so that curtain animation can run. For
  example, call this inside a loop if you want the curtain to move.  

- `keep_window_open()` keeps the window open until the user closes it.

You need **Python 3** with **tkinter** (normally comes with Python).

**Example**:

```python
import stage

stage.curtain_up()   # Curtain moves up until fully open

stage.keep_window_open()
```

**Challenge**: Make the curtain move up all the way to the top, pause for a
second, then move down all the way to the bottom. To pause for 1 second, use
`time.sleep(1)`.

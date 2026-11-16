"""
A row of closed boxes drawn with turtle graphics. Each box hides a number.
The only way to find out what is in a box is to call open_box(i), which
plays a short animation of the lid opening and returns the number inside.

A counter at the top of the window shows how many boxes have been opened.
Under the counter, a line says whether the numbers are in random order or in
sorted order.
If you call show_target(target), the window also shows the number you are
searching for, and if you call show_title(title) it shows a title of your
choice, such as the name of the algorithm being used. If you call
wait_for_start(), a Start button appears and your program waits until it is
clicked. wait_for_button(label) does the same with a label of your choice.

Typical use:

    import boxes

    boxes.setup(10)             # 10 boxes, numbers in random order
    value = boxes.open_box(0)   # open the first box and get its number
    print(value)

When your program reaches its end, the window stays open and a Restart
button appears. Clicking Restart runs your program again from the beginning.
Close the window to finish.

Use boxes.setup(10, sorted=True) to put the numbers in order from smallest
to largest.

The numbers in the boxes are whole numbers, and they are all different (no
duplicates). With 10 or fewer boxes they are from 1 to 99. With more than 10
boxes they go higher: up to 199 for 20 boxes, and up to 999 for 100 boxes.
0 and negative numbers are never in a box.
"""

import atexit
import os
import random
import runpy
import sys
import time
import tkinter
import traceback
import turtle

# Module-level state
_values = []          # the hidden number in each box
_is_open = []         # True/False for each box: has it been opened?
_is_highlighted = []  # True/False for each box: has it been highlighted?
_num_opened = 0       # how many times open_box has been called
_target = None        # the number being searched for (set by show_target)
_has_target = False   # True once show_target has been called
_title = ""           # the title at the top of the window (set by show_title)
_speed = 3            # 1 = slowest, 10 = fastest, 0 = no animation

# Turtles (created in setup)
_box_pens = []        # one turtle for each box
_counter_pen = None   # turtle that writes the counter
_button_pen = None    # turtle that draws the Start and Restart buttons
_button_clicked = False
_main_file = None     # the file name of the program that is using this module
_canvas = None        # the window's drawing area, used to check it's still open
_exit_registered = False

# Layout (calculated in setup)
_box_size = 60
_boxes_per_row = 10
_left_x = 0.0
_top_y = 0.0
_row_height = 0.0
_counter_y = 0.0
_button_y = 0.0             # y of the centre of the Start/Restart button

# Drawing constants
_GAP = 8                    # space between boxes
_MAX_PER_ROW = 25
_LID_OPEN_ANGLE = 105       # how far the lid swings up, in degrees
_ANIMATION_FRAMES = 8
_CLOSED_COLOR = "#C8964B"
_OPEN_COLOR = "#FFF8DC"
_HIGHLIGHT_COLOR = "#9BE28A"
_OUTLINE_COLOR = "#6B4A1B"
_QUESTION_COLOR = "#8A632A"
_BUTTON_WIDTH = 110
_BUTTON_HEIGHT = 36
_START_COLOR = "#2E8B57"
_SORTED_COLOR = "#1E7B45"    # green text when the numbers are sorted
_RANDOM_COLOR = "#B5541B"    # orange text when they are not
_RESTART_COLOR = "#2F5FA8"


def setup(n=10, sorted=False, values=None):
    """
    Open the window and draw n closed boxes, each hiding a different number.

    The numbers are chosen at random. They are all different (no duplicates),
    and are whole numbers from 1 up to 99, or up to 10*n - 1 if that is
    bigger (for example, 1 to 999 when n is 100). 0 and negative numbers are
    never used.

    n:      how many boxes to draw.
    sorted: if False (the default) the numbers are in random order. If True,
            the numbers are in order from smallest to largest.
    values: optional list of your own values to hide in the boxes. If you
            give this, n is ignored and one box is drawn for each value.
            Your values are used exactly as given, so they can include
            duplicates, 0, or negative numbers.
    """
    global _values, _is_open, _is_highlighted, _num_opened, _has_target
    global _title
    global _box_pens, _counter_pen, _button_pen, _canvas, _exit_registered
    global _main_file

    if values is not None:
        new_values = list(values)
    else:
        if n < 1:
            raise ValueError("setup: n must be at least 1")
        biggest = max(100, 10 * n)
        new_values = random.sample(range(1, biggest), n)
    if len(new_values) < 1:
        raise ValueError("setup: there must be at least 1 box")
    if sorted:
        new_values.sort()
        order_text = "Numbers are in sorted order: smallest to largest"
        order_color = _SORTED_COLOR
    elif values is not None:
        order_text = "Numbers are in the order they were given"
        order_color = _RANDOM_COLOR
    else:
        order_text = "Numbers are in random order"
        order_color = _RANDOM_COLOR

    _values = new_values
    _is_open = [False] * len(_values)
    _is_highlighted = [False] * len(_values)
    _num_opened = 0
    _has_target = False
    _title = ""

    width, height = _calculate_layout(len(_values))
    turtle.setup(width=width, height=height)
    turtle.clearscreen()
    turtle.title("Boxes")
    turtle.tracer(0, 0)  # no screen updates until turtle.update()
    _canvas = turtle.getcanvas()
    if not _exit_registered:
        # When the program finishes, keep the window open until it is closed
        _main_file = getattr(sys.modules.get("__main__"), "__file__", None)
        if _main_file is not None:
            _main_file = os.path.abspath(_main_file)
        atexit.register(_keep_window_open)
        _exit_registered = True

    # The line saying what order the numbers are in never changes, and
    # neither do the index numbers under the boxes, so draw them once
    label_pen = _make_pen()
    label_pen.pencolor(order_color)
    label_pen.goto(0, _counter_y - 24)
    label_pen.write(order_text, align="center", font=("Arial", 13, "italic"))
    label_pen.pencolor("gray40")
    for i in range(len(_values)):
        x, y = _box_corner(i)
        label_pen.goto(x + _box_size / 2, y - _label_font_size() * 2)
        label_pen.write(str(i), align="center",
                        font=("Arial", _label_font_size(), "normal"))

    _box_pens = []
    for i in range(len(_values)):
        _box_pens.append(_make_pen())
        _draw_box(i, 0)

    _counter_pen = _make_pen()
    _button_pen = _make_pen()
    _draw_counter()
    turtle.update()


def open_box(i):
    """
    Open box i (the first box is box 0) and return the number inside it.
    Every call adds 1 to the "Boxes opened" counter.
    """
    global _num_opened
    _check_index(i, "open_box")

    _num_opened += 1
    _draw_counter()

    if _speed > 0:
        # Swing the lid up a little at a time
        pause = (0.8 / _speed) / _ANIMATION_FRAMES
        _is_open[i] = False
        for frame in range(1, _ANIMATION_FRAMES):
            _draw_box(i, _LID_OPEN_ANGLE * frame / _ANIMATION_FRAMES)
            turtle.update()
            time.sleep(pause)

    _is_open[i] = True
    _draw_box(i, _LID_OPEN_ANGLE)
    turtle.update()
    if _speed > 0:
        time.sleep(pause * 2)
    return _values[i]


def wait_for_start():
    """
    Show a Start button at the bottom of the window and wait until the user
    clicks it. Then the button disappears and your program carries on.
    """
    wait_for_button("Start")


def wait_for_button(label):
    """
    Show a button with the given label at the bottom of the window, and wait
    until the user clicks it. Then the button disappears and your program
    carries on. For example, boxes.wait_for_button("Next") pauses the program
    so the boxes can be looked at before it moves on.
    """
    _check_setup("wait_for_button")
    try:
        _show_button_and_wait(str(label), _START_COLOR)
    except (turtle.Terminator, tkinter.TclError):
        # The window was closed instead of clicking the button: end the program
        raise SystemExit


def show_title(title):
    """
    Show a title in large letters at the top of the window, for example
    the name of the algorithm being used: boxes.show_title("Linear search").
    Call it again to change the title. The title stays until it is changed
    or setup is called again.
    """
    global _title
    _check_setup("show_title")
    _title = str(title)
    _draw_counter()
    turtle.update()


def show_target(target):
    """
    Show "Searching for: <target>" at the top of the window, so anyone
    watching knows what number the program is looking for.
    """
    global _target, _has_target
    _check_setup("show_target")
    _target = target
    _has_target = True
    _draw_counter()
    turtle.update()


def num_boxes():
    """Return how many boxes there are."""
    return len(_values)


def num_opened():
    """Return how many times open_box has been called."""
    return _num_opened


def random_value():
    """
    Return a number that is hidden in one of the boxes, chosen at random.
    Useful for picking a target to search for.
    """
    _check_setup("random_value")
    return random.choice(_values)


def highlight_box(i):
    """Colour box i green, for example to show where the target was found."""
    _check_index(i, "highlight_box")
    _is_highlighted[i] = True
    if _is_open[i]:
        _draw_box(i, _LID_OPEN_ANGLE)
    else:
        _draw_box(i, 0)
    turtle.update()


def close_all():
    """
    Close every box, remove any highlighting, and set the counter back to 0.
    The numbers in the boxes stay the same, and so do the target shown by
    show_target and the title shown by show_title.
    """
    global _num_opened
    _check_setup("close_all")
    _num_opened = 0
    for i in range(len(_values)):
        _is_open[i] = False
        _is_highlighted[i] = False
        _draw_box(i, 0)
    _draw_counter()
    turtle.update()


def set_speed(speed):
    """
    Set how fast the boxes open: 1 is slowest, 10 is fastest, and 0 means
    no animation at all (boxes open instantly). The default is 3.
    """
    global _speed
    if speed < 0 or speed > 10:
        raise ValueError("set_speed: speed must be from 0 to 10")
    _speed = speed


#
# Helper functions (not meant to be called from outside this module)
#

def _keep_window_open():
    """
    Called automatically when the program ends. Shows a Restart button and
    waits. If Restart is clicked, the program is run again from the
    beginning. This repeats until the user closes the window.
    """
    while True:
        try:
            still_open = _canvas.winfo_exists()
        except Exception:
            still_open = False   # the window has already been closed
        if not still_open:
            return

        if _main_file is None:
            # Not run from a file, so there is no program to run again
            turtle.done()
            return

        try:
            _show_button_and_wait("Restart", _RESTART_COLOR)
        except (turtle.Terminator, tkinter.TclError):
            return               # the window was closed

        print()
        try:
            runpy.run_path(_main_file, run_name="__main__")
        except (SystemExit, turtle.Terminator, tkinter.TclError):
            return               # the window was closed during the run
        except Exception:
            traceback.print_exc()   # show the error, then offer Restart again


def _show_button_and_wait(label, color):
    """
    Draw a button with the given label at the bottom of the window, and wait
    until the user clicks it. Then remove the button.
    """
    global _button_clicked
    _button_clicked = False
    _draw_button(label, color)
    turtle.onscreenclick(_handle_click)
    while not _button_clicked:
        turtle.update()      # also lets the window notice mouse clicks
        time.sleep(0.02)
    turtle.onscreenclick(None)
    _button_pen.clear()
    turtle.update()


def _handle_click(x, y):
    """Called by turtle when the window is clicked at (x, y)."""
    global _button_clicked
    if abs(x) <= _BUTTON_WIDTH / 2 and abs(y - _button_y) <= _BUTTON_HEIGHT / 2:
        _button_clicked = True


def _draw_button(label, color):
    """Draw a button with the given label at the bottom of the window."""
    pen = _button_pen
    pen.clear()
    pen.pensize(2)
    pen.pencolor("gray25")
    pen.fillcolor(color)
    pen.goto(-_BUTTON_WIDTH / 2, _button_y - _BUTTON_HEIGHT / 2)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    for side in range(2):
        pen.forward(_BUTTON_WIDTH)
        pen.left(90)
        pen.forward(_BUTTON_HEIGHT)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.goto(0, _button_y - 12)
    pen.pencolor("white")
    pen.write(label, align="center", font=("Arial", 16, "bold"))


def _check_setup(function_name):
    """Give a helpful error if setup() hasn't been called yet."""
    if len(_box_pens) == 0:
        raise RuntimeError(function_name + ": call boxes.setup() first")


def _check_index(i, function_name):
    """Give a helpful error if i is not a valid box index."""
    _check_setup(function_name)
    if type(i) != int:
        raise TypeError(function_name + ": the box index must be an int, not "
                        + repr(i))
    if i < 0 or i >= len(_values):
        raise IndexError(function_name + ": there is no box " + str(i)
                         + " (boxes are numbered 0 to "
                         + str(len(_values) - 1) + ")")


def _make_pen():
    """Return a new hidden turtle with its pen up."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    return pen


def _calculate_layout(n):
    """Choose the box size and positions for n boxes. Return the window size."""
    global _box_size, _boxes_per_row, _left_x, _top_y, _row_height, _counter_y
    global _button_y
    if n <= 10:
        _box_size = 60
    elif n <= 16:
        _box_size = 44
    else:
        _box_size = 30
    _boxes_per_row = min(n, _MAX_PER_ROW)
    num_rows = (n + _boxes_per_row - 1) // _boxes_per_row

    # Each row needs room for the open lid above the box and the index below
    _row_height = 2 * _box_size + 34
    row_width = _boxes_per_row * (_box_size + _GAP) - _GAP
    width = max(420, row_width + 80)
    # 158 for the text at the top, 60 for the button at the bottom
    height = 158 + num_rows * _row_height + 60

    _left_x = -row_width / 2
    _counter_y = height / 2 - 112
    _button_y = -height / 2 + 36
    _top_y = _counter_y - 36 - _box_size   # top edge of the first row of boxes
    return width, height


def _box_corner(i):
    """Return (x, y) of the bottom-left corner of box i."""
    column = i % _boxes_per_row
    row = i // _boxes_per_row
    x = _left_x + column * (_box_size + _GAP)
    y = _top_y - row * _row_height - _box_size
    return x, y


def _value_font_size():
    return _box_size * 3 // 10


def _label_font_size():
    return max(8, _box_size // 5)


def _draw_box(i, lid_angle):
    """
    Redraw box i with its lid lifted lid_angle degrees (0 means closed).
    The number is shown only if the box is marked as open.
    """
    pen = _box_pens[i]
    pen.clear()
    x, y = _box_corner(i)
    size = _box_size

    if _is_highlighted[i]:
        fill = _HIGHLIGHT_COLOR
    elif _is_open[i]:
        fill = _OPEN_COLOR
    else:
        fill = _CLOSED_COLOR

    # Body of the box
    pen.pensize(2)
    pen.pencolor(_OUTLINE_COLOR)
    pen.fillcolor(fill)
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    for side in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()
    pen.penup()

    # What's written in the box: the number if open, otherwise a question mark
    font_size = _value_font_size()
    pen.goto(x + size / 2, y + size / 2 - font_size * 0.8)
    if _is_open[i]:
        pen.pencolor("black")
        pen.write(str(_values[i]), align="center",
                  font=("Arial", font_size, "bold"))
    elif lid_angle == 0:
        pen.pencolor(_QUESTION_COLOR)
        pen.write("?", align="center", font=("Arial", font_size, "bold"))

    # Lid: a thick line hinged at the top-left corner of the box
    pen.pencolor(_OUTLINE_COLOR)
    pen.pensize(max(3, size // 12))
    pen.goto(x, y + size)
    pen.setheading(lid_angle)
    pen.pendown()
    pen.forward(size)
    pen.penup()


def _draw_counter():
    """Rewrite the title, target, and "Boxes opened" lines at the top."""
    _counter_pen.clear()
    if _title != "":
        _counter_pen.goto(0, _counter_y + 60)
        _counter_pen.pencolor("black")
        _counter_pen.write(_title, align="center", font=("Arial", 20, "bold"))
    if _has_target:
        _counter_pen.goto(0, _counter_y + 28)
        _counter_pen.pencolor("#1F4E9C")
        _counter_pen.write("Searching for: " + str(_target), align="center",
                           font=("Arial", 16, "bold"))
    _counter_pen.goto(0, _counter_y)
    _counter_pen.pencolor("black")
    _counter_pen.write("Boxes opened: " + str(_num_opened), align="center",
                       font=("Arial", 16, "bold"))

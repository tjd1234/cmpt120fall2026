"""
Clock face drawn with turtle graphics.
Second, minute, and hour hands can be set to specific angles.
Tick marks at each minute; 12, 3, 6, 9 are thicker quarter-hour ticks.
"""

import turtle

# Module-level state: angles in degrees (0 = 12 o'clock, increasing clockwise)
_second_hand_angle = 0.0
_minute_hand_angle = 0.0
_hour_hand_angle = 0.0

# Window position (None = center on that axis)
_window_startx = None
_window_starty = None

# After first draw: static turtle (face, ticks, numbers) and hands turtle
_pen_static = None
_pen = None

# Tick visibility (both on by default)
_show_minute_ticks = True   # the 60 small ticks at each minute
_show_quarter_ticks = True   # the 4 thicker ticks at 12, 3, 6, 9
_show_numbers = True        # the 1–12 hour numbers around the face

# Drawing constants
_FACE_RADIUS = 120
_TICK_LENGTH = 15          # quarter-hour (12, 3, 6, 9) tick length
_HOUR_TICK_LENGTH = 10     # hour (1, 2, 4, 5, ...) tick – longer than minute, shorter than quarter
_MINUTE_TICK_LENGTH = 6    # minute tick length (thinner, shorter)
_NUMBER_RADIUS = 95        # radius for hour numbers (inside the ticks)
_SECOND_HAND_LENGTH = 95
_MINUTE_HAND_LENGTH = 75
_HOUR_HAND_LENGTH = 50


def _angle_to_heading(angle):
    """Convert clock angle (0 = 12 o'clock, clockwise) to turtle heading (0 = east)."""
    return 90 - angle


def set_second_hand_angle(angle):
    """Set the angle of the second hand in degrees (0 = 12 o'clock, clockwise)."""
    global _second_hand_angle
    _second_hand_angle = float(angle)
    if _pen is not None:
        _redraw_hands()


def set_minute_hand_angle(angle):
    """Set the angle of the minute hand in degrees (0 = 12 o'clock, clockwise)."""
    global _minute_hand_angle
    _minute_hand_angle = float(angle)
    if _pen is not None:
        _redraw_hands()


def set_hour_hand_angle(angle):
    """Set the angle of the hour hand in degrees (0 = 12 o'clock, clockwise)."""
    global _hour_hand_angle
    _hour_hand_angle = float(angle)
    if _pen is not None:
        _redraw_hands()


def set_window_position(startx, starty):
    """
    Set the position of the window on the screen when the clock is drawn.
    startx: horizontal position in pixels (left edge); None to center horizontally.
    starty: vertical position in pixels (top edge); None to center vertically.
    """
    global _window_startx, _window_starty
    _window_startx = startx
    _window_starty = starty


def set_show_minute_ticks(show):
    """Turn the 60 minute tick marks on (True) or off (False). Default is on."""
    global _show_minute_ticks
    _show_minute_ticks = bool(show)
    if _pen is not None:
        _redraw_full()


def set_show_quarter_ticks(show):
    """Turn the quarter-hour tick marks (12, 3, 6, 9) on (True) or off (False). Default is on."""
    global _show_quarter_ticks
    _show_quarter_ticks = bool(show)
    if _pen is not None:
        _redraw_full()


def set_show_numbers(show):
    """Turn the hour numbers (1–12) around the face on (True) or off (False). Default is on."""
    global _show_numbers
    _show_numbers = bool(show)
    if _pen is not None:
        _redraw_full()


def _redraw_hands():
    """Clear and redraw only the hands (keeps face, ticks, numbers unchanged to avoid jitter)."""
    _pen.clear()
    _draw_hand(_pen, _second_hand_angle, _SECOND_HAND_LENGTH, width=1, color="red")
    _draw_hand(_pen, _minute_hand_angle, _MINUTE_HAND_LENGTH, width=2)
    _draw_hand(_pen, _hour_hand_angle, _HOUR_HAND_LENGTH, width=3)
    turtle.update()


def _redraw_full():
    """Clear and redraw static layer and hands (for visibility changes)."""
    _pen_static.clear()
    _draw_face_and_ticks(_pen_static)
    _redraw_hands()


def _draw_face_and_ticks(pen):
    """Draw the circular face and tick marks at every minute (quarter-hour ticks thicker)."""
    pen.penup()
    pen.goto(0, -_FACE_RADIUS)
    pen.setheading(0)
    pen.pendown()
    pen.circle(_FACE_RADIUS)

    for minute in range(60):
        is_quarter = (minute % 15) == 0  # 12, 3, 6, 9 o'clock
        # At quarter positions: draw quarter tick if on, else minute tick if on (so all 60 have a tick when only minute ticks are on)
        if is_quarter and _show_quarter_ticks:
            length = _TICK_LENGTH
            pen.pensize(2)
        elif _show_minute_ticks:
            is_hour = (minute % 5) == 0  # 12, 1, 2, 3, ... (quarter handled above)
            if is_hour:
                length = _HOUR_TICK_LENGTH
                pen.pensize(1)
            else:
                length = _MINUTE_TICK_LENGTH
                pen.pensize(1)
        else:
            continue
        clock_angle = minute * 6  # 0, 6, 12, ... 354
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(_angle_to_heading(clock_angle))
        pen.forward(_FACE_RADIUS - length)
        pen.pendown()
        pen.forward(length)

    if _show_numbers:
        _draw_numbers(pen)


def _draw_numbers(pen):
    """Draw the hour numbers 1–12 around the face."""
    pen.penup()
    pen.pencolor("black")
    for n in range(1, 13):
        # 12 at top (0°), 1 at 30°, 2 at 60°, ... 11 at 330°
        angle = (n % 12) * 30
        pen.goto(0, 0)
        pen.setheading(_angle_to_heading(angle))
        pen.forward(_NUMBER_RADIUS)
        pen.goto(pen.xcor(), pen.ycor() - 8)  # nudge down so numbers sit visually centered
        pen.write(str(n), align="center", font=("Arial", 14, "normal"))


def _draw_hand(pen, angle, length, width=1, color="black"):
    """Draw a single hand from center at the given clock angle."""
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(_angle_to_heading(angle))
    pen.pensize(width)
    pen.pencolor(color)
    pen.pendown()
    pen.forward(length)


def draw_clock():
    """
    Draw the clock face (circle and tick marks at every minute;
    quarter-hour ticks thicker) and the second, minute, and hour hands.
    Returns immediately; the display updates whenever a hand setter is called.
    Call turtle.done() after draw_clock() to keep the window open and responsive.
    """
    global _pen_static, _pen
    turtle.setup(width=450, height=450, startx=_window_startx, starty=_window_starty)
    turtle.tracer(0, 0)  # no screen updates until turtle.update()
    static_pen = turtle.Turtle()
    static_pen.hideturtle()
    static_pen.speed(0)
    _pen_static = static_pen
    _draw_face_and_ticks(static_pen)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    _pen = pen
    _draw_hand(pen, _second_hand_angle, _SECOND_HAND_LENGTH, width=1, color="red")
    _draw_hand(pen, _minute_hand_angle, _MINUTE_HAND_LENGTH, width=2)
    _draw_hand(pen, _hour_hand_angle, _HOUR_HAND_LENGTH, width=3)

    turtle.update()

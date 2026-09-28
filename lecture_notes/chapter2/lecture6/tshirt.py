"""Draw a t-shirt and print short messages on it.

There are three lines. Each line holds at most 10 characters.

Example:
    import tshirt

    tshirt.print_line1("Hello")
    tshirt.print_line2("to the")
    tshirt.print_line3("world!")
"""

import atexit
import tkinter as tk
from tkinter import font as tkfont

LINE_WIDTH = 10

_BG = "#E8F2F8"
_SHIRT = "#3B9AE1"
_SHIRT_OUTLINE = "#1F6FAD"
_SHADOW = "#C5D4E0"
_COLLAR = "#2B7FBF"
_STITCH = "#7EC0EE"
_SLEEVE_HOLE = "#1A5F8C"
_TEXT = "#FFFFFF"

_root = tk.Tk()
_root.title("My T-Shirt")
_root.resizable(False, False)
_root.configure(bg=_BG)

_canvas = tk.Canvas(
    _root,
    width=500,
    height=560,
    bg=_BG,
    highlightthickness=0,
)
_canvas.pack()


def _offset(points, dx, dy):
    return [(x + dx, y + dy) for x, y in points]


# Outline of a short-sleeved crew-neck shirt, drawn clockwise
# from the left sleeve.
_SHIRT_POINTS = [
    (90, 128),
    (58, 158),
    (70, 200),
    (148, 208),
    (155, 452),
    (178, 472),
    (250, 480),
    (322, 472),
    (345, 452),
    (352, 208),
    (430, 200),
    (442, 158),
    (410, 128),
    (332, 116),
    (302, 106),
    (278, 148),
    (250, 158),
    (222, 148),
    (198, 106),
    (168, 116),
]


def _draw_shirt():
    _canvas.create_polygon(
        _offset(_SHIRT_POINTS, 8, 10),
        fill=_SHADOW,
        outline="",
        smooth=True,
    )
    _canvas.create_polygon(
        _SHIRT_POINTS,
        fill=_SHIRT,
        outline=_SHIRT_OUTLINE,
        width=3,
        smooth=True,
    )
    # Collar trim
    _canvas.create_arc(
        196,
        92,
        304,
        168,
        start=200,
        extent=140,
        style=tk.ARC,
        width=7,
        outline=_COLLAR,
    )
    # Open cuffs so the sleeves look like you can put arms through them
    _canvas.create_oval(
        62,
        134,
        92,
        196,
        fill=_SLEEVE_HOLE,
        outline=_SHIRT_OUTLINE,
        width=3,
    )
    _canvas.create_oval(
        408,
        134,
        438,
        196,
        fill=_SLEEVE_HOLE,
        outline=_SHIRT_OUTLINE,
        width=3,
    )
    # Hem stitching
    _canvas.create_line(
        172,
        455,
        250,
        464,
        328,
        455,
        fill=_STITCH,
        width=2,
        smooth=True,
    )


_draw_shirt()

# A 10-character field, left-aligned, centered as a block on the shirt
# so students can center text themselves by padding with spaces.
_text_font = tkfont.Font(family="Courier", size=26, weight="bold")
_text_left = 250 - (_text_font.measure("0") * LINE_WIDTH) / 2 + 24

_line_ids = [
    _canvas.create_text(
        _text_left,
        250 + i * 42,
        text="",
        fill=_TEXT,
        font=_text_font,
        anchor="w",
    )
    for i in range(3)
]

_root.update_idletasks()
_root.lift()
try:
    _root.attributes("-topmost", True)
    _root.after_idle(_root.attributes, "-topmost", False)
except tk.TclError:
    pass
_root.update()


def _clip(text):
    return str(text)[:LINE_WIDTH]


def _set_line(index, text):
    _canvas.itemconfig(_line_ids[index], text=_clip(text))
    _root.update()


def print_line1(text):
    """Print up to 10 characters on the first line of the t-shirt."""
    _set_line(0, text)


def print_line2(text):
    """Print up to 10 characters on the second line of the t-shirt."""
    _set_line(1, text)


def print_line3(text):
    """Print up to 10 characters on the third line of the t-shirt."""
    _set_line(2, text)


def _keep_window_open():
    try:
        if _root.winfo_exists():
            _root.mainloop()
    except tk.TclError:
        pass


atexit.register(_keep_window_open)

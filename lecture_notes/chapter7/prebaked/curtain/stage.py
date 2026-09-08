"""
Stage with a curtain. Use curtain_up() and curtain_down() to move the curtain
slowly and smoothly. Use get_height() to read the current position.
Behind the curtain is a simple scene (house and flower).
"""

import tkinter as tk

# Module-level window and canvas
_window = None
_canvas = None
_curtain_left = None
_curtain_right = None
_curtain_height = 0.0  # 0.0 = closed, 1.0 = fully open
_animation_after_id = None
_canvas_height = 400
_canvas_width = 600
_stage_height = 60

# Animation: step size and delay (ms) for smooth movement
_CURTAIN_STEP = 0.02
_CURTAIN_DELAY_MS = 35


def _draw_backdrop(canvas):
    """Draw the scene behind the curtain: sky, sun, house, flower."""
    w, h = _canvas_width, _canvas_height
    stage_top = h - _stage_height

    # Sky gradient (light blue)
    canvas.create_rectangle(0, 0, w, stage_top, fill="#87CEEB", outline="")

    # Sun
    canvas.create_oval(w - 80, 40, w - 20, 100, fill="#FFD700", outline="#FFA500", width=2)

    # House body
    house_x, house_y = 80, stage_top - 180
    canvas.create_rectangle(house_x, house_y + 80, house_x + 160, house_y + 180, fill="#DEB887", outline="#8B4513", width=2)
    # Roof
    canvas.create_polygon(house_x - 10, house_y + 80, house_x + 80, house_y + 20, house_x + 170, house_y + 80, fill="#8B4513", outline="#5D3A1A", width=2)
    # Door
    canvas.create_rectangle(house_x + 65, house_y + 120, house_x + 95, house_y + 180, fill="#8B4513", outline="#5D3A1A", width=2)
    # Window
    canvas.create_rectangle(house_x + 20, house_y + 100, house_x + 50, house_y + 130, fill="#ADD8E6", outline="#4682B4", width=2)

    # Flower on the ground (right side of stage)
    fx = 420
    ground_y = stage_top  # top of stage = ground level
    stem_height = 55
    bloom_center_y = ground_y - stem_height  # top of stem / center of flower
    # Stem (from bloom down to ground)
    canvas.create_line(fx, bloom_center_y, fx, ground_y, fill="#228B22", width=4)
    # Leaves
    canvas.create_oval(fx - 8, bloom_center_y + 20, fx + 8, bloom_center_y + 40, fill="#228B22", outline="#006400")
    # Petals
    for dx, dy in [(0, -15), (12, -5), (8, 10), (-8, 10), (-12, -5)]:
        canvas.create_oval(fx + dx - 12, bloom_center_y + dy - 12, fx + dx + 12, bloom_center_y + dy + 12, fill="#FF69B4", outline="#FF1493", width=1)
    canvas.create_oval(fx - 10, bloom_center_y - 10, fx + 10, bloom_center_y + 10, fill="#FFD700", outline="#FFA500", width=1)


def _draw_stage(canvas):
    """Draw the stage (floor) at the bottom."""
    w, h = _canvas_width, _canvas_height
    canvas.create_rectangle(0, h - _stage_height, w, h, fill="#8B4513", outline="#5D3A1A", width=3)
    # Wood planks effect
    for i in range(0, w, 40):
        canvas.create_line(i, h - _stage_height, i, h, fill="#5D3A1A", width=1)


def _draw_curtains(canvas, curtain_bottom_y):
    """Draw left and right curtain panels from top to curtain_bottom_y."""
    w, h = _canvas_width, _canvas_height
    view_height = h - _stage_height
    y_bottom = max(0, min(curtain_bottom_y, view_height))

    left = canvas.create_polygon(
        0, 0,
        w * 0.49, 0,
        w * 0.48, y_bottom,
        0, y_bottom,
        fill="#8B0000", outline="#4B0000", width=2
    )
    right = canvas.create_polygon(
        w * 0.51, 0,
        w, 0,
        w, y_bottom,
        w * 0.52, y_bottom,
        fill="#8B0000", outline="#4B0000", width=2
    )
    return left, right


def _apply_curtain_height():
    """Redraw the curtain at the current _curtain_height."""
    global _curtain_left, _curtain_right
    if _canvas is None or _curtain_left is None:
        return
    view_height = _canvas_height - _stage_height
    curtain_bottom_y = view_height * (1.0 - _curtain_height)
    _canvas.delete(_curtain_left)
    _canvas.delete(_curtain_right)
    _curtain_left, _curtain_right = _draw_curtains(_canvas, curtain_bottom_y)
    if _window is not None:
        _window.update()


def _ensure_window(after_ready=None):
    """Create the stage window if it does not exist yet. Idempotent."""
    global _window, _canvas, _curtain_left, _curtain_right
    if _window is not None:
        return
    _window = tk.Tk()
    _window.title("Stage with curtain")
    _canvas = tk.Canvas(_window, width=_canvas_width, height=_canvas_height, bg="#87CEEB")
    _canvas.pack()

    _draw_backdrop(_canvas)
    _draw_stage(_canvas)
    _curtain_left, _curtain_right = _draw_curtains(_canvas, _canvas_height - _stage_height)

    if after_ready is not None:
        _window.after(500, after_ready)


def _step_up():
    """One step of curtain-up animation. Schedules next step if not fully up."""
    global _curtain_height, _animation_after_id
    _curtain_height = min(1.0, _curtain_height + _CURTAIN_STEP)
    _apply_curtain_height()
    if _curtain_height < 1.0 and _window is not None:
        _animation_after_id = _window.after(_CURTAIN_DELAY_MS, _step_up)
    else:
        _animation_after_id = None


def _step_down():
    """One step of curtain-down animation. Schedules next step if not fully down."""
    global _curtain_height, _animation_after_id
    _curtain_height = max(0.0, _curtain_height - _CURTAIN_STEP)
    _apply_curtain_height()
    if _curtain_height > 0.0 and _window is not None:
        _animation_after_id = _window.after(_CURTAIN_DELAY_MS, _step_down)
    else:
        _animation_after_id = None


def curtain_up():
    """Move the curtain slowly and smoothly up until it is completely open."""
    global _animation_after_id
    _ensure_window()
    if _window is None:
        return
    if _animation_after_id is not None:
        _window.after_cancel(_animation_after_id)
        _animation_after_id = None
    if _curtain_height >= 1.0:
        return
    _step_up()


def curtain_down():
    """Move the curtain slowly and smoothly down until it is completely closed."""
    global _animation_after_id
    _ensure_window()
    if _window is None:
        return
    if _animation_after_id is not None:
        _window.after_cancel(_animation_after_id)
        _animation_after_id = None
    if _curtain_height <= 0.0:
        return
    _step_down()


def get_height():
    """Return the current curtain height: 0.0 = fully closed, 1.0 = fully open."""
    return _curtain_height


def update():
    """Process pending events so that curtain animation can run.
    Call this in a loop when waiting for the curtain to move (e.g. while get_height() < 1.0)."""
    if _window is not None:
        _window.update()


def get_window():
    """Return the stage window (for use with after() etc.). Returns None until the window has been created."""
    return _window


def keep_window_open(after_ready=None):
    """Ensure the stage window exists, then run the main loop (window stays open until the user closes it)."""
    _ensure_window(after_ready)
    _window.mainloop()


if __name__ == "__main__":
    keep_window_open()

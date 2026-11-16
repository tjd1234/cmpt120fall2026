# Lecture Plan: Linear Search and Binary Search with `boxes.py`

A 50-minute lecture for CMPT 120. Students have just finished lists and
dictionaries. The lecture uses `boxes.py` for both algorithms and follows the
usual four-question format (`q1.py` to `q4.py`).

## Goals

By the end, students should be able to:

- write linear search with a loop, and say how many boxes it opens in the
  best, worst, and average case
- explain why binary search needs the data to be in sorted order
- trace binary search by hand using `low`, `high`, and `mid`
- compare the two: about n opens versus about 7 opens for 100 boxes

## Before class

- Put `boxes.py` in the lecture zip alongside the question files.
- Run `boxes_intro.py` and `q1_sol.py` once on the classroom machine to check
  that the window, the Start button, and the animation all work there.
- Draw this empty table on the board, to be filled in during the lecture:

  | Boxes     | Linear search (worst case) | Binary search (worst case) |
  |-----------|----------------------------|----------------------------|
  | 10        |                            |                            |
  | 100       |                            |                            |
  | 1000      |                            |                            |
  | 1,000,000 |                            |                            |

## Timeline

| Time  | Segment              | What happens                                             |
|-------|----------------------|----------------------------------------------------------|
| 0-6   | 1. Meet the boxes    | Live-code a short program: set up, open, highlight       |
| 6-16  | 2. q1: linear search | Students write the search loop; class predicts the count |
| 16-20 | 3. q2: not there     | Search for a number that is in no box                    |
| 20-25 | 4. Scaling up        | 100 boxes; fill in the linear column of the table        |
| 25-30 | 5. Bridge            | Higher/lower guessing game; open one sorted box          |
| 30-42 | 6. q3: binary search | Trace on the board, then code it together                |
| 42-47 | 7. q4: the race      | Same boxes, same target, both searches                   |
| 47-50 | 8. Wrap-up           | The trade-off, and two exit questions                    |

---

## Segment 1: Meet the boxes (0-6 min)

The aim is for students to know how to use `boxes.py` before they are asked
to write a search with it. Live-code the program below one step at a time,
running it after each step. The finished version is in `boxes_intro.py`.

**Step 1: make the boxes.**

```python
import boxes

boxes.setup(5)
boxes.show_title("Meet the boxes")

boxes.done()
```

**Say:** "This makes a window with 5 closed boxes. Each box hides a number,
and the boxes are numbered underneath starting at 0, just like a list.
`boxes.done()` is always the last line of the program: it keeps the window
open and shows a Restart button. Clicking Restart runs the whole program
again with new numbers in the boxes." `show_title` puts a title at the top
of the window.

In the steps below, add the new code *above* the `boxes.done()` line, so
that `boxes.done()` stays last.

**Step 2: open a box.**

```python
value = boxes.open_box(0)
print("Box 0 holds", value)
```

**Say:** "`open_box` does two things: it opens the box in the window, and it
returns the number inside so the program can use it. This is the *only* way
the program can find out what is in a box."

**Point out:** the "Boxes opened" counter at the top went up to 1.

**Step 3: open another box and highlight it.**

```python
value = boxes.open_box(3)
print("Box 3 holds", value)

boxes.highlight_box(3)
```

**Ask:** "What will the counter say now?" (2)

**Step 4: how many boxes?**

```python
print("Number of boxes:", boxes.num_boxes())
```

**Ask:** "What do you think happens if I call `boxes.open_box(5)`?" Try it:
the program stops with an error saying there is no box 5, because the boxes
are numbered 0 to 4.

**Step 5: show the q1 starter.** Open `q1.py` and run it without changing
anything. Point out the two new things in the window: the "Searching for"
line and the Start button. Click Start: nothing happens.

**Say:** "The program has picked a number that is in one of these boxes, but
it doesn't know which one. Your job is to write the code that finds it."

## Segment 2: q1, write linear search (6-16 min)

**Start file gives students:**

```python
import boxes

boxes.setup(10)
boxes.show_title("Linear search")
target = boxes.pick_target_value()
boxes.show_target(target)
boxes.wait_for_start()

# TODO: open the boxes one at a time, starting at box 0, until you find
# target. Highlight the box it is in, and print its index.


boxes.done()   # keep the window open and show the Restart button
```

**Functions to leave on a slide** (all three were shown in segment 1):

- `boxes.open_box(i)` opens box `i` and returns the number inside
- `boxes.num_boxes()` returns how many boxes there are
- `boxes.highlight_box(i)` colours box `i` green

**Sample solution:**

```python
found_index = -1
i = 0
while i < boxes.num_boxes() and found_index == -1:
    value = boxes.open_box(i)
    if value == target:
        found_index = i
    i += 1

boxes.highlight_box(found_index)
print("Found", target, "in box", found_index)
```

**Watch for:** a `for` loop that finds the target but keeps opening the rest
of the boxes. The counter makes this visible: it always ends at 10. Use it to
ask "Did it need to open those last boxes?"

**Debrief (last 3 minutes):** Run the solution three times, using the Restart
button to get a new target each time. Before each click of Start, ask the
class to predict how many boxes will open, and write the final counts on the
board.

**Ask:**

- "What's the smallest count we could ever get?" (1: the target is in box 0)
- "What's the largest?" (10: the target is in the last box)
- "If we ran it many times, what would the count be on average?" (about half
  the boxes)

**Say:** "This is called *linear search*: start at the first box and check
them one at a time, in order, until you find what you're looking for."

## Segment 3: q2, the target isn't there (16-20 min)

**Say:** "What if the number we want isn't in any box?" The numbers in the
boxes are always 1 or bigger, so 0 is never there.

**Task:** Change the program so that `target = 0`. It should print "0 is not
in any box" and must not crash.

**Sample solution (the ending changes):**

```python
if found_index == -1:
    print(target, "is not in any box")
else:
    boxes.highlight_box(found_index)
    print("Found", target, "in box", found_index)
```

**Watch for:** calling `boxes.highlight_box(-1)`, which stops with an error
saying there is no box -1.

**Point to draw out:** the counter ends at 10. *Not* finding something is the
most expensive case, because every box has to be opened to be sure.

## Segment 4: Scaling up (20-25 min)

**Do:** Change the setup to 100 boxes and speed up the animation:

```python
boxes.setup(100)
boxes.set_speed(10)
```

Run it with `target = 0` so every box opens. It takes about ten seconds.

**Do:** Fill in the linear column of the board table: 10, 100, 1000,
1,000,000.

**Say:** "Double the number of boxes and you double the work. For a million
boxes at this speed we'd be here for more than a day."

## Segment 5: Bridge to binary search (25-30 min)

**Do:** Play higher/lower with one student. "I'm thinking of a number from 1
to 100." Always guess the middle of what's left. It takes at most 7 guesses.
Write each guess and the remaining range on the board.

**Ask:** "Why can't we search the boxes like that?" (The numbers in the boxes
are in random order, so opening one box tells us nothing about the others.)

**Do:** Change the setup, run it, and open the middle box:

```python
boxes.setup(100, sorted=True)
value = boxes.open_box(49)
print(value)
```

**Ask:** "The numbers now go from smallest to largest. Suppose our target is
bigger than the number in box 49. What do we know about boxes 0 to 48?" (The
target can't be in any of them: one open has ruled out half the boxes.)

## Segment 6: q3, binary search (30-42 min)

**Trace on the board first.** Use 10 sorted boxes with made-up numbers, for
example:

| index | 0 | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|-------|---|----|----|----|----|----|----|----|----|----|
| value | 4 | 11 | 23 | 30 | 42 | 57 | 61 | 78 | 85 | 93 |

Search for 78, keeping a table of `low`, `high`, and `mid`:

| low | high | mid | value in box mid | decision               |
|-----|------|-----|------------------|------------------------|
| 0   | 9    | 4   | 42               | too small: low = 5     |
| 5   | 9    | 7   | 78               | found it               |

Then search for 23 (three opens: boxes 4, 1, 2) so students see both
directions.

**Then code it together.** Type the outline and have students supply the
three branches:

```python
import boxes

boxes.setup(100, sorted=True)
boxes.show_title("Binary search")
target = boxes.pick_target_value()
boxes.show_target(target)
boxes.wait_for_start()

low = 0
high = boxes.num_boxes() - 1
found_index = -1
while low <= high and found_index == -1:
    mid = (low + high) // 2
    value = boxes.open_box(mid)
    if value == target:
        found_index = mid
    elif value < target:
        low = mid + 1
    else:
        high = mid - 1

if found_index == -1:
    print(target, "is not in any box")
else:
    boxes.highlight_box(found_index)
    print("Found", target, "in box", found_index)

boxes.done()
```

**Make this mistake on purpose:** first write `low = mid` instead of
`low = mid + 1`. For some targets the program opens the same box over and
over, and the counter keeps climbing. Ask the class why, then fix it. (Close
the window to stop the program.)

**Remind them:** `//` is integer division, so `mid` is always a whole number.

## Segment 7: q4, the race (42-47 min)

**Task:** On the same 100 sorted boxes and the same target, run linear search,
then binary search, and print both counts.

```python
boxes.show_title("Linear search")
boxes.wait_for_start()

# ... linear search here ...
linear_count = boxes.num_opened()

boxes.wait_for_button("Next")
boxes.close_all()
boxes.show_title("Binary search")

# ... binary search here ...
binary_count = boxes.num_opened()

print("Linear search opened", linear_count, "boxes")
print("Binary search opened", binary_count, "boxes")

boxes.done()
```

**Do:** Fill in the binary column of the board table:

| Boxes     | Linear search (worst case) | Binary search (worst case) |
|-----------|----------------------------|----------------------------|
| 10        | 10                         | 4                          |
| 100       | 100                        | 7                          |
| 1000      | 1000                       | 10                         |
| 1,000,000 | 1,000,000                  | 20                         |

**Say:** "Every time the number of boxes doubles, binary search needs just one
more open. Our `words.txt` file has 113,783 words. Linear search might check
all of them. Binary search needs at most 17."

## Segment 8: Wrap-up (47-50 min)

**Say:** "Binary search is much faster, but it only works when the data is in
sorted order. Linear search works on anything. So how do we get data into
sorted order, and how much work is that? That's next lecture."

**Exit questions:**

1. How many boxes would binary search open, at most, for 2000 sorted boxes?
   (11: one more than for 1000)
2. Why can't binary search be used on boxes in random order?

---

## If time runs short

The squeeze is segment 6. Live-code binary search completely instead of
having students supply the branches, and move q4 (the race) to homework. The
board table still delivers the comparison.

## If there is extra time

- Ask students to predict, before running, which boxes binary search will
  open for a target they choose from the board trace.
- Search for a number that isn't there (0) with binary search and compare the
  count with linear search's 100.

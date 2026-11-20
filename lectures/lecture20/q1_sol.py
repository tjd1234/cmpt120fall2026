# q1_sol.py

"""
You're building a puzzle game for little kids. Each round shows the player a
word with its first and last letters swapped, and they have to work out the real
word. The main code has already been written for you: see below.

However, it doesn't work because the scramble function is not defined. Define
the scramble function that returns (not prints!) the scrambled version of the
word. To scramble a word, swap the first and last letters. If the word has fewer
than 2 characters, return the word unchanged. For example, scramble("python")
returns "nythop" and scramble("a") returns "a".

Don't change any of the given code: just add the scramble function.

Sample Run

```
Kid Scramble!

What is the real word for: ootatp? potato
Correct!

What is the real word for: tarroc? carot
Incorrect. The real word is carrot.

What is the real word for: whrot? Throw
Incorrect. The real word is throw.

What is the real word for: eppla? apple
Correct!

What is the real word for: aananb? banana
Correct!

You got 3 out of 5 correct.
```

Given Code

```python
words = ["potato", "carrot", "throw", "apple", "banana"]

print("Kid Scramble!")

correct = 0
for w in words:
    scrambled = scramble(w)
    guess = input(f"\nWhat is the real word for: {scrambled}? ").strip()
    if guess == w:
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect. The real word is {w}.")

print(f"\nYou got {correct} out of {len(words)} correct.")
```
"""

def scramble(word):
    if len(word) < 2:
        return word
    return word[-1] + word[1:-1] + word[0]

words = ["potato", "carrot", "throw", "apple", "banana"]

print("Kid Scramble!")

correct = 0
for w in words:
    scrambled = scramble(w)
    guess = input(f"\nWhat is the real word for: {scrambled}? ").strip()
    if guess == w:
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect. The real word is {w}.")

print(f"\nYou got {correct} out of {len(words)} correct.")
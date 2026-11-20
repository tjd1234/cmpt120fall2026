# Writing Code with AI: Tic Tac Toe

In this activity, your task is to use AI to make a graphical and mouse-based
[Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game using Python.

You can use any AI you want, such as [ChatGPT](https://chatgpt.com) or
[Gemini](https://gemini.google.com). You do *not* need to use a paid AI service.

You should write English prompts to guide the AI to write the program. The
output should be plain Python that could run on anyone's computer if they have
Python installed with turtle graphics. Do not let the AI use any extra libraries
or frameworks that don't come with Python by default.

You should probably not try to make the program in one big prompt. Instead, ask
the AI to make the basic game, and then add features one at a time with separate
prompts.

For each prompt, you should save the program the AI creates. For example, call
the first version of the program `tictactoe_1.py`. Then when you ask the AI to
add a new feature, save the new version of the program as `tictactoe_2.py`,
the next new version as `tictactoe_3.py`, etc.

Save your prompts to the AI by copying-and-pasting them into
[prompts.txt](prompts.txt).

## Required features

- graphical board and pieces

- click with mouse to place pieces

- human plays versus the computer; the strategy for how the computer plays is up
  to you

- when the game starts, who goes first is chosen randomly

- automatically check for a winner or draw

- when the game is over, display who the winner is, or if it is a draw; if there
  is a winner, then draw a line through the winning squares

- show a score line that shows the number of wins and losses for the human, and
  the number of draws

- when the game is over, let the user play again

## Optional features

In addition to the basic requirements, please add at least one other good,
cool, or fun feature you can think of. A few examples:

- when the human wins, make some animated fireworks

- let the human choose from different opponents:
  - **Smarty**: never loses, and always wins if possible
  - **Randy**: always wins if possible, and always blocks if necessary, but
    otherwise always chooses a random empty square
  - **Loopy**: tries as hard as it can to lose, i.e. it never makes a winning
    move (unless it's forced to), and it tries to set up the human to win

- make it look like you are playing against a character, e.g. here's an old TV
  commercial for [Tic Tac Toe against a
  chicken](https://www.youtube.com/watch?v=4q5je2fpXVQ)

- add an undo button that allows the human to undo their last move (and the
  computer's last move)

- add an option to play [an alternative version of Tic Tac
  Toe](https://en.wikipedia.org/wiki/Tic-tac-toe_variants), e.g.:

  - **Reverse Tic Tac Toe**: whoever gets three in a row first loses.

  - **Three Piece Tic Tac Toe**: each player gets only three pieces. From their
    fourth turn onward, players take their turn by moving their oldest piece to
    a new empty location on the board.

  - **Ten Square Tic Tac Toe**: make the board 10 squares instead of 9. How
    exactly you do this is up to you, e.g. you could add one extra square beside
    one of the existing outside squares.

## What to Submit

Please submit:

- *All* your `tictactoe_N.py` files. Please include all versions of your
  program. The marker will assume that the version with the highest N is the
  final version, and will probably only run that one.

- A screenshot of your game in action that we can share with the class.

- A filled-in copy of [prompts.txt](prompts.txt) that has the text prompts you
  used to guide the AI.

- A filled-in copy of [questions.txt](questions.txt). Please answer all the
  questions.

Compress these files into a single zip file named `AI_activity.zip`, and then
submit the zip file to Canvas.

## Marking

- **8 marks** for the basic requirements (1 mark for each required feature)

- **2 marks** for the optional feature; a low-effort optional feature might not
  get full marks

- **1 mark** for the screenshot

- **1 mark** for [prompts.txt](prompts.txt) filled in with the prompts you used
  to guide the AI

- **2 marks** for answering all the questions in [questions.txt](questions.txt);
  low-effort answers might not get full marks

- **1 mark** for submitting the zip file with the required name and containing
  just the required files.

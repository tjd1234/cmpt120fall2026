# counting_votes.py
# Counting Votes
#
# This file shows how to use dictionaries to count the votes, i.e. strings in a list.

votes = ['bob', 'alice', 'bob', 'alice', 'alice', 'dan', 'dan']

# TODO 1: Make an empty dictionary called tally.

# TODO 2: Loop through the votes and increment that candidate's vote count by 1.
# If the candidate is not already in the tally, first add them and set their
# vote count to 0. Print the tally to verify it's correct.

# TODO 3: Print the names of all candidates without any duplicates.

# TODO 4: Re-do the previous task, but print the names in alphabetical order.

# TODO 5: Find the winner. Do the following:
# - Initialize a variable called winner to the empty string, ''
# - Initialize a variable called most_votes to 0
# - Loop through the tally, and for each candidate:
#   - If their vote count is greater than most_votes, update most_votes to
#     their vote count, and update winner to their name.
# - Print the winner.

# TODO 6: Print all candidates and their votes, sorted from highest to lowest
# vote count.
#
# Do it as follows:
# - Initialize an empty list called count_name
# - Loop through the tally, and for each candidate:
#   - Add the list [tally[name], name] to count_name
# - Sort count_name, and then reverse it using .reverse() (so highest vote count
#   is first)
# - Using a loop, print vote count and name of each candidate

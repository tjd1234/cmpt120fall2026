# counting_votes.py
# Counting Votes
#
# This file shows how to use dictionaries to count the votes, i.e. strings in a list.

votes = ['bob', 'alice', 'bob', 'alice', 'alice', 'dan', 'dan']

# TODO 1: Make an empty dictionary called tally.
tally = {}

# TODO 2: Loop through the votes and increment that candidate's vote count by 1.
# If the candidate is not already in the tally, first add them and set their
# vote count to 0. Print the tally to verify it's correct.
for name in votes:
    if name not in tally:
        tally[name] = 0
    tally[name] += 1

print(tally)

# TODO 3: Print the names of all candidates without any duplicates.
print('All candidates:', tally.keys())

# TODO 4: Re-do the previous task, but print the names in alphabetical order.
candidates = list(tally.keys())
candidates.sort()
print('Sorted candidates:', candidates)

# TODO 5: Find the winner. Do the following:
# - Initialize a variable called winner to the empty string, ''
winner = ''

# - Initialize a variable called most_votes to 0
most_votes = 0

# - Loop through the tally, and for each candidate:
for name in tally:
    #   - If their vote count is greater than most_votes, update most_votes to
    #     their vote count, and update winner to their name.
    if tally[name] > most_votes:
        most_votes = tally[name]
        winner = name

# - Print the winner.
print('winner:', winner, most_votes)

# TODO 6: Print all candidates and their votes, sorted from highest to lowest
# vote count.
#
# Do it as follows:

# - Initialize an empty list called count_name
count_name = []

# - Loop through the tally, and for each candidate:
for name in tally:
    #   - Add the list [tally[name], name] to count_name
    count_name.append([tally[name], name])

# - Sort count_name, and then reverse it using .reverse() (so highest vote count
#   is first)
count_name.sort()
count_name.reverse()

# - Using a loop, print vote count and name of each candidate
for pair in count_name:
    print(pair[0], pair[1])

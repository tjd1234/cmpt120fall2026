# q4_sol.py

"""
The student council president election has five candidates: Ava, Ben, Cara,
Dana, and Evan. The file votes.txt contains all the votes cast, one per line.
Any name other than one of these five candidates is invalid and counts as a
spoiled vote.

Write a program that reads the votes from votes.txt and counts how many votes
each candidate received, and then prints out the results from most votes to
least votes. Also include the number of spoiled votes. If there is a tie, then
order doesn't matter.

For example, suppose votes.txt contains this:

```
Cara
Dana
Ava
Dana
Ben
Carl
Ben
Ben
Ava
Scooby
Ben
```

Then the program should print:

```
Ben: 4
Dana: 2
Ava: 2
Cara: 1
Evan: 0
Spoiled votes: 2
```
"""
#
# initialize all the counts to 0
#
votes = {'Ava': 0, 'Ben': 0, 'Cara': 0, 'Dana': 0, 'Evan': 0}
spoiled_votes = 0

#
# open the file and read the names (one per line)
#
print("Reading votes from votes.txt...")
vote_file = open("votes.txt", 'r') # open the file for reading
for name in vote_file:
    name = name.strip() # remove whitespace from the name
    if name in votes:
        votes[name] += 1 # increment the count for this candidate
    else:
        spoiled_votes += 1 # increment the count for spoiled votes

#
# make list of pairs of [count, name] so we can sort them
#
name_vote = []
for name in votes:
    pair = [votes[name], name] # create a pair of [count, name]
    name_vote.append(pair)     # add it to the end of the list of all pairs
    
# .sort() sorts the list of pairs from least votes to most votes
name_vote.sort()
print('name_vote:', name_vote)

# reverse the order so they go from most votes to least votes
name_vote.reverse() 

#
# print the results
#
for count, name in name_vote:
    print(f"{name}: {count}")
print(f"Spoiled votes: {spoiled_votes}")

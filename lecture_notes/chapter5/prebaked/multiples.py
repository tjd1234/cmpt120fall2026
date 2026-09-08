# multiples.py

#
# Write a program that prints all the numbers from 1 to 100 that are multiples
# of both 3 and 5, but not multiples of 2.
#

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0 and i % 2 != 0:
        print(i)

# change.py

#How many nickels do you have? 2
#How many quarters do you have? 3
#You have $0.85 dollars.

# get input
nickels = int(input('How many nickels do you have? '))
quarters = int(input('How many quarters do you have? '))

# process input
cents = 5 * nickels + 25 * quarters
dollars = cents / 100

# print output
print(f'You have ${dollars:.2f} dollars.')


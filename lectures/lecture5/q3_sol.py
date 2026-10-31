# q3_sol.py

nickels = int(input('How many nickels do you have? '))
quarters = int(input('How many quarters do you have? '))
total_cents = nickels * 5 + quarters * 25

# use an f-string to format the total to 2 decimal places
print(f'You have ${total_cents / 100:.2f} dollars.')
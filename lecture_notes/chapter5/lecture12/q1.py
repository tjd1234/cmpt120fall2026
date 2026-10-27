# q1.py

"""
A movie theatre sells discount tickets for $7 instead of the regular $14. To get
the discount, both of these must be true:

1. The movie is an afternoon show, which means it starts at or after 12:00
   (noon) and *before* 17:00 (5pm). Show times are by the hour and use the
   24-hour clock, e.g. 12 is 12pm (noon), 13 is 1pm, 14 is 2pm, etc.

2. The customer is 12 or younger, 65 or older, or has a student card.

Write a program that asks for the show's starting hour (0 to 23), the customer's
age, and whether they have a student card (y or n), and then prints the ticket
price. 

**Don't** ask a question if the ticket price is already determined.

Sample Run 1

```
Show start hour (0-23)? 14
Age? 20 
Student card (y/n)? y 

Your ticket costs $7.
```

Sample Run 2

```
Show start hour (0-23)? 19 

Your ticket costs $14.
```

Sample Run 3

```
Show start hour (0-23)? 13
Age? 70

Your ticket costs $7.
```
"""

hour = int(input('Show start hour (0-23)? '))

if hour < 12 or hour >= 17:
    print('\nYour ticket costs $14.')
else: # 12 <= hour < 17 (rule 1 satisfied)
    age = int(input('Age? '))
    if age <= 12 or age >= 65:
        print('\nYour ticket costs $7.')
    else: # 12 < age < 65
        # Student card (y/n)? y
        student_card = input('Student card (y/n)? ')
        if student_card == 'y':
            print('\nYour ticket costs $7.')
        else:
            print('\nYour ticket costs $14.')
        
        




           

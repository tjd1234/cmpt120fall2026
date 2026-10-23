# q1_sol.py

"""
Write a program to help a restaurant cashier calculate the total cost of a meal
for a group of people. The program asks the price of each customer's meal, and
then prints the total cost of the entire meal. The cashier types "done" when all
meals have been entered.

If there are more than 3 customers in the group, then a service charge of 20% is
automatically added to the total cost.

All prices printed by the program should be formatted in standard dollar format,
i.e. starting with `$` and to exactly 2 decimal places.

Sample Run 1

```
Price of meal 1: 10.00
Price of meal 2: 15.99
Price of meal 3: 20.00
Price of meal 4: 25.00
Price of meal 5: done

      Subtotal: $70.00
Service charge: $14.00
         Total: $84.00
```

Sample Run 2

```
Price of meal 1: 6.50
Price of meal 2: 20.00
Price of meal 3: done

      Subtotal: $26.50
         Total: $26.50
```
"""
#
# initialize variables
#
meal_num = 1
subtotal = 0.0

#
# get the prices of the meals
#
meal_price = float(input("Price of meal 1: "))
while meal_price != "done":
    subtotal += float(meal_price)
    meal_num += 1
    meal_price = input(f"Price of meal {meal_num}: ")

#
# Add a 20% service charge if there are more than 3 customers
#
total = subtotal
service_charge = 0.0
if meal_num > 4: # careful: 4 is correct here, not 3! 
    service_charge = subtotal * 0.2
    total += service_charge

#
# print the results
#
print()
print(f"      Subtotal: ${subtotal:.2f}")
if service_charge > 0:
    print(f"Service charge: ${service_charge:.2f}")
print(f"         Total: ${total:.2f}")

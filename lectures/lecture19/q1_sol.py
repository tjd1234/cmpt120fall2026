# q1_sol.py

"""
A small campus cafe stores each customer's order in two lists, e.g.:

```python
items  = ['latte', 'muffin', 'tea']
prices = [5.25, 3.5, 2.75]
```

items[i] is the name of something the customer ordered, and prices[i] is its
price. So the latte costs $5.25, the muffin $3.50, and the tea $2.75.

Write a function print_receipt(items, prices) that prints a receipt to the
screen:

- The first line is the cafe name: The Java Hut Cafe
- The following lines have the form "item: price", i.e. each item and its
  price.
- The last line is the total of all the prices: "Total: total"

Show all prices with exactly 2 digits after the decimal point. The function
print to the screen and not return anything.

Sample Run

If items and prices are as above, calling print_receipt(items, prices) 
should print:

```
Java Hut Cafe

latte: $5.25
muffin: $3.50
tea: $2.75

Total: $11.50
```
"""

def print_receipt(items, prices):
    print("The Java Hut Cafe\n")
    num_items = len(items)
    for i in range(num_items):
        item = items[i]
        price = prices[i]
        print(f"{item}: ${price:.2f}")
    total = sum(prices)
    print(f"\nTotal: ${total:.2f}")

#
# main program
#
items  = ['latte', 'muffin', 'tea']
prices = [5.25, 3.5, 2.75]
print_receipt(items, prices)

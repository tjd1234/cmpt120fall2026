# q1.py

"""
A small campus cafe stores each customer's order in two lists, e.g.:

```python
items  = ['latte', 'muffin', 'tea']
prices = [5.25,    3.5,      2.75]
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

Modify the previous program so that in addition to printing the receipt on the
screen, it also writes the receipt to a text file called "receipt.txt". The
contents of "receipt.txt" should be the same as the printed output.
"""

#items  = ['latte', 'muffin', 'tea']
#prices = [5.25,    3.5,      2.75]
def print_receipt(items, prices):
    output_file = open('receipt.txt', 'w') # w means open for writing
    print('Java Hut Cafe\n')
    output_file.write('Java Hut Cafe\n\n')
    num_items = len(items)
    for i in range(num_items):
        item, price = items[i], prices[i]
        print(f'{item}: ${price:.2f}')
        output_file.write(f'{item}: ${price:.2f}\n')
    total = sum(prices)
    print(f'\nTotal: ${total:.2f}')
    output_file.write(f'\nTotal: ${total:.2f}\n')
    output_file.close()


items  = ['latte', 'muffin', 'tea']
prices = [5.25,    3.5,      2.75]
print_receipt(items, prices)





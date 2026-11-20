# q2_sol.py

"""
Modify the previous program so that in addition to printing the receipt on the
screen, it also writes the receipt to a text file called "receipt.txt". The
contents of "receipt.txt" should be the same as the printed output.

Sample Run

Suppose items and prices are defined like this:

```python
items = ['latte', 'muffin', 'tea']
prices = [5.25, 3.5, 2.75]
```

Then calling print_receipt(items, prices) prints the following both on the
screen, and to the file "receipt.txt":

```
Java Hut Cafe

latte: $5.25
muffin: $3.50
tea: $2.75

Total: $11.50
```
"""

def print_receipt(items, prices):
    output_file = open("receipt.txt", "w")  # "w" means open for writing
    print("The Java Hut Cafe\n")
    output_file.write("The Java Hut Cafe\n\n") # note the extra \n at the end
    num_items = len(items)
    for i in range(num_items):
        item = items[i]
        price = prices[i]
        print(f"{item}: ${price:.2f}")
        output_file.write(f"{item}: ${price:.2f}\n") # note the \n at the end
    total = sum(prices)
    print(f"\nTotal: ${total:.2f}")
    output_file.write(f"\nTotal: ${total:.2f}\n") # note the \n at the end
    output_file.close()
#
# main program
#
items  = ['latte', 'muffin', 'tea']
prices = [5.25, 3.5, 2.75]
print_receipt(items, prices)

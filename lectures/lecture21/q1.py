# q1.py

"""
Sold Out!

Orders for the campus coffee shop are kept in a list of strings, oldest order
first. For example:

```python 
orders = ['latte', 'muffin', 'oat latte', 'tea', 'oat latte', 
          'scone', 'oat latte']
```

Sometimes the shop runs out of an item, and so those items need to be removed
from the order list. The barista also needs to know how many orders were
removed.

Write a function called remove_sold_out(orders, bad_item) that:

- removes *every* copy of bad_item from the list orders, using the list's remove
  method
- returns (not prints!) the number of items removed

The function should change the orders list itself in-place, i.e. it should NOT
make a new list.

Your remove_sold_out(orders, bad_item) function should work with code like this:

```
orders = ['latte', 'muffin', 'oat latte', 'tea', 'oat latte', 
          'scone', 'oat latte']
n = remove_sold_out(orders, 'oat latte')
print(n)        # prints 3
print(orders)   # prints ['latte', 'muffin', 'tea', 'scone']

# orders is now: ['latte', 'muffin', 'tea', 'scone']
n = remove_sold_out(orders, 'hot chocolate')
print(n)        # prints 0
print(orders)   # prints ['latte', 'muffin', 'tea', 'scone']
```
"""

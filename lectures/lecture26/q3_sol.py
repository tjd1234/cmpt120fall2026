# q3_sol.py

"""
Consider the following program, which calculates the average of a list of quiz
scores minus the lowest score:

```
scores = [4, 8, 6, 2, 10]
lowest = my_min(scores) # 2 is lowest
average = (sum(scores) - lowest) / (len(scores) - 1)
print(average)  # 7.0
```

Write the my_min function: it should return the lowest number on a list of
numbers. Do NOT use Python's built-in min function (calculate it using variables
and a loop).
"""

def my_min(lst):
    smallest_so_far = lst[0]
    for num in lst:
        if num < smallest_so_far:
            smallest_so_far = num
    return smallest_so_far

scores = [4, 8, 6, 2, 10]
lowest = my_min(scores) # 2 is lowest
average = (sum(scores) - lowest) / (len(scores) - 1)
print(f'Quiz average: {average}')  # 7.0

# q2.py

"""
You have your first job as a software engineer! You work at a children's
education software company, and you are in charge of checking if a word contains
the letter *m*. The previous developer (who has been promoted to work with *n*)
has left you with this function:

```python
def has_m_print(word):
    for letter in word:
        if letter == 'm':
            print('this word has an "m"')

# test code
has_m_print('tumble')  # this word has an "m"
has_m_print('Map')     # nothing printed 
has_m_print('apple')   # nothing printed 
has_m_print('')        # nothing printed
```

Your task is to update the function as follows:

- make it find both lowercase `m` and uppercase `M`

- instead of printing a message, have it return `True` if the word contains an m
  (either lowercase or uppercase), and `False` otherwise; you should probably
  change the name of the function

- convert and update the test cases to work with this new function

"""

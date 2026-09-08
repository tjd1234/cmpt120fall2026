# dictionaries1_sol.py

# TODO 1: Make an empty dictionary called age, then print it and print its
# length.
age = {}
print(age)  # {}
print(len(age))  # 0

# TODO 2: Re-make the age dictionary, and this time add the following as
# key:value pairs:
# - Marge is 34
# - Homer is 36
# - Bart is 10
#
# Then print the dictionary and its length.
age = {"Marge": 34, "Homer": 36, "Bart": 10}

print(age)  # {'Marge': 34, 'Homer': 36, 'Bart': 10}
print(len(age))  # 3

# TODO 3: Print Marge, Homer's, and Bart's ages. What if you try to print Lisa's age?
print(age["Marge"])  # 34
print(age["Homer"])  # 36
print(age["Bart"])  # 10
# print(age['Lisa']) # KeyError: 'Lisa'

# TODO 4: Add Lisa's age (she's 8)to the dictionary. The other names and ages
# should stay the same.
age["Lisa"] = 8
print(age)

# TODO 5: Increase Marge's age as follows: set it to 35, and then increase it by
# 1 using +=. Print the dictionary.
age["Marge"] = 35
age["Marge"] += 1
print(age)

# TODO 6: Young Homer, who is 12, shows up. He has exactly the same name as the
# current Homer. What happens if you add the young Homer to the dictionary?
# Print the result.
age["Homer"] = 12
print(age)  # {'Marge': 35, 'Homer': 12, 'Bart': 10, 'Lisa': 8}
# Old Homer is gone!

# TODO 7: Print just the names of the dictionary.
print(age.keys())  # dict_keys(['Marge', 'Homer', 'Bart', 'Lisa'])

# TODO 8: Print just the ages of the dictionary.
print(age.values())  # dict_values([35, 12, 10, 8])

# TODO 9: Print the key:value pairs of the dictionary as list of pairs.
print(age.items())  # dict_items([('Marge', 35), ('Homer', 12), ('Bart', 10), ('Lisa', 8)])

# TODO 10: How an you test if Marge is a name in the dictionary? What about Maggie?
print("Marge" in age)  # True

# TODO 11: How can you test if someone is 10 years old? 50 years old?
print(10 in age.values())  # True
print(50 in age.values())  # False

# TODO 12: Check the course notes on dictionaries to learn about how they use
# hashing to allow super-fast key lookups (but slow value lookups).

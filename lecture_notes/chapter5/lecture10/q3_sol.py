# q3_sol.py

"""
The community pool charges $8 for admission, unless you fall into one of these
categories:

- Seniors, aged 65 or older, pay $5

- Children, aged 6 through 12, pay $4

- Kids under 6 get in free

Write a program that asks the user their age and then prints their price of
admission.

Sample run 1
```
Enter your age: 65
Admission: $5
```

Sample run 2
```
Enter your age: 22
Admission: $8
```

Sample run 3
```
Enter your age: 5
Admission: free!
```
"""

age = int(input("Enter your age: "))
if age >= 65:
    print("Admission: $5")
elif 13 <= age <= 64:
    print("Admission: $8")
elif 6 <= age <= 12:
    print("Admission: $4")
else:
    print("Admission: free!")

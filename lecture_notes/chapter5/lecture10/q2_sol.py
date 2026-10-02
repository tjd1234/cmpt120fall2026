# q2_sol.py

"""
Write a program that asks the user to enter the temperature and then tells them
what to wear according to these rules:

- If the temperature is 10 degrees or less, they should wear a warm coat.

- If the temperature is greater than 10 degrees and less than 25 degrees, they
  should wear a light jacket.

- If the temperature is greater than 25 degrees, they should wear a t-shirt.


Sample run 1
```
Enter the temperature: 10
Wear a warm coat.
```

Sample run 2
```
Enter the temperature: 20
Wear a light jacket.
```

Sample run 3
```
Enter the temperature: 31.5
Wear a t-shirt.
```
"""

temp = float(input("Enter the temperature: "))
if temp <= 10:
    print("Wear a warm coat.")
elif 10 < temp < 25:
    print("Wear a light jacket.")
else:
    print("Wear a t-shirt.")

# hurricane.py

#
# Write a program that asks the user for the wind speed, and prints its category
# (or that it's not a hurricane) and if it's major.
#

#
# The Saffir-Simpson hurricane scale ranks the severity of hurricanes based on
# their wind speed. The scale ranges from 1 to 5 (most severe):
#
# Category 1 hurricane: wind speed 119 to less than 154 km/h
# Category 2 hurricane: wind speed 154 to less than 178 km/h
# Category 3 hurricane: wind speed 178 to less than 209 km/h
# Category 4 hurricane: wind speed 209 to less than 252 km/h
# Category 5 hurricane: wind speed 252 km/h or more
#
# A wind speed of less than 119 km/h is not considered to be a hurricane.
# Category 3 and higher are “major” hurricanes.
#

speed = float(input("Enter the wind speed in km/h: "))
if speed < 119:
    print(f'A wind speed of {speed} km/h is not a hurricane.')
elif speed < 154:
    print(f'A wind speed of {speed} km/h is a Category 1 hurricane.')
elif speed < 178:
    print(f'A wind speed of {speed} km/h is a Category 2 hurricane.')
elif speed < 209:
    print(f'A wind speed of {speed} km/h is a Category 3 hurricane.')
    print('It is a major hurricane.')
elif speed < 252:
    print(f'A wind speed of {speed} km/h is a Category 4 hurricane.')
    print('It is a major hurricane.')
else:
    print(f'A wind speed of {speed} km/h is a Category 5 hurricane.')
    print('It is a major hurricane.')

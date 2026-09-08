# password_checker2.py

import turtle

screen = turtle.Screen()
screen.title("Password Entry")

password = turtle.textinput("Password", "Enter a password:")
while password != 'swordfish':
    password = turtle.textinput("Invalid", "Invalid password. Try again.")

screen.bye() # shut the window
print("Password accepted!")

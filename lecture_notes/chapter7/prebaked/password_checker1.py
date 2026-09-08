# password_checker1.py

import turtle

def main():
    screen = turtle.Screen()
    screen.title("Password Entry")

    while True:
        password = turtle.textinput("Password", "Enter a password:")
        if password == 'swordfish':
            screen.bye() # shut the window
            print("Password accepted!")
            return # jump out of the function
        turtle.textinput("Invalid", "Invalid password. Try again.")

main()

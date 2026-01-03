# Program to ask for input and check length of input

username = input("Enter your name:")

if len(username) > 2:
    print(f"Welcome, {username}!")
else:
    print("Your name must be at least 3 characters long")
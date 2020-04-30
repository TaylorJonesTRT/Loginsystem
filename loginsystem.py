import json
import sys
import hashlib


user_details = {}

hasher = hashlib.sha256()

with open('user_credentials.json', 'r') as f:
    user_details = json.load(f)

while True:
    print("Welcome to the new and sophisticated login system!")

    choice = input("What would you like to do? \n [1]LOGIN \n [2]REGISTER \n")

    while choice == "1":
        username_login = input("Pleaser enter your username: ")
        if username_login in user_details.keys():
            password_login = input(
                "Please enter your password: ").encode('utf-8')
            password_login = hasher.update(password_login)
            if username_login in user_details and user_details[username_login] == password_login:
                print("You are now loggged in! Welcome back!")
                print("Now exiting program")
                sys.exit()
            else:
                print("Sorry, that was the wrong password. Try again.")
        else:
            print("Sorry, that username does not exist. Please try again")

    while choice == "2":
        print("Please choose a username, it can be your email address or a plain username")
        username_registration = input("")
        print("Please enter a password")
        password_registration = input("").encode('utf-8')
        user_details[username_registration] = hasher.update(
            password_registration)
        with open('user_credentials.json', 'w') as fp:
            json.dump(user_details, fp, indent=4)
        print("Thank you for registering! You may now sign in!")
        break

    decision = input(
        "What would you like to do now? Continue or Exit?").lower()

    if decision == "continue":
        continue
    else:
        sys.exit()

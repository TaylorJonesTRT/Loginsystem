user_details = {
    'Test': 'Test123'
}

print("Welcome to the new and sphoisticated login system!")

while True:
    choice = input("What would you like to do? \n [1]LOGIN \n [2]REGISTER \n")
    while choice == "1":
        username_login = input("Pleaser enter your username: ")
        if username_login in user_details.keys():
            password_login = input("Please enter your password: ")
            if (username_login in user_details and user_details[username_login] == password_login):
                print("You are now loggged in! Welcome back!")
                break
            else:
                print("Sorry, that was the wrong password. Try again.")
        else:
            print("Sorry, that username does not exist. Please try again")
            continue

    while choice == "2":
        print("Please choose a username, it can be your email address or a plain username")
        username_registragion = input("")
        print("Please enter a password")
        password_registration = input("")
        user_details[username_registragion] = password_registration
        print("Thank you for registering! You may now sign in!")
        break

    decision = input("What would you like to do now? Continue or Exit?")

    if decision == "Continue" or "continue":
        continue
    else:
        break

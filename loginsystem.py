user_details = {
    'Test': 'Test123'
}

print("Welcome to the new and sphoisticated login system!")
choice = input("What would you like to do? \n [1]LOGIN \n [2]REGISTER \n")

while choice == "1":
    username = input("Pleaser enter your username: ")
    if username in user_details.keys():
        password = input("Please enter your password: ")
    else:
        print("Sorry, that username does not exist. Please try again")
        continue

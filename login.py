password = "123897"

while True:
    username = input("Enter username: ")
    user_password = input("Enter password: ")

    if user_password == password:
        print("Successfully logged in")
        break
    else:
        print("Please enter correct password")

username = "Prerna"
password = "12345"
attempts = 0

while attempts < 3:
    user_username = input("Enter username: ")
    user_password = input("Enter password: ")

    if user_username == username or user_password == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Try again.")
        attempts += 1

if attempts == 3:
    print("You have exceeded  max number of attempts. You are blocked.")
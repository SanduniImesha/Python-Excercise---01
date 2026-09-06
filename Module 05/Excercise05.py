correct_username = "python"
correct_password = "rules"
attempts = 0
logged_in = False

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")
    attempts += 1
    if username == correct_username and password == correct_password:
        print("Welcome")
        logged_in = True
        break
    else:
        print("Incorrect username or password, try again.")

if not logged_in:
    print("Access denied")
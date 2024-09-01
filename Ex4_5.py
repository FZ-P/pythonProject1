def authenticate():
    correct_username = "python"
    correct_password = "rules"
    attempts = 0
    while attempts < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == correct_username and password == correct_password:
            print("Welcome")
            return
        else:
            print("Incorrect username or password.")
            attempts += 1

    print("Access denied.")

authenticate()

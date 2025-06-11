USERNAME = "admin"
PASSWORD = "12345"
isLogin = False
while not isLogin:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
        isLogin = True
    else:
        print("Invalid username or password. Please try again.")
#Login Page using while loop
username=""
password=""
while username != "admin" and password != "mysecret":
    username = input("Enter Username:")
    password = input("Enter Password:")
    print("login successful")
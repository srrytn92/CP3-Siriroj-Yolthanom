print("Please Login")
USERNAME = input("Username : ")
PASSWORD = input("Password : ")
while USERNAME != "admin" or PASSWORD != "123456":
    print("Username or Password Is Wrong Please Login Again")
    USERNAME = input("Username : ")
    PASSWORD = input("Password : ")
print("!!!----WELCOME----!!!")

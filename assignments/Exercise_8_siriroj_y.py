USERNAME = input("Username : ")
PASSWORD = input("Password : ")
if USERNAME == "admin" and PASSWORD == "123456":
    print(" Welcome to shop")
    print("1.Marbo Grape 150 THB")
    print("2.Marbo Red 150 THB")
    print("3.Toasty 300 THB")
    print("4.Vanilla Custard 300 THB")
    print("Please Selected Product ")
    ProductSelected = int(input("Selected Your Product : "))
    if ProductSelected == 1:
        amount = int(input("Amount : "))
        print("1.Marbo Grape 150 THB",amount,amount*150,"THB")
    elif ProductSelected == 2:
        amount = int(input("Amount : "))
        print("2.Marbo Red 150 THB",amount,amount*150,"THB")
    elif ProductSelected == 3:
        amount = int(input("Amount : "))
        print("3.Toasty 300 THB",amount,amount*300,"THB")
    elif ProductSelected == 4:
        amount = int(input("Amount : "))
        print("4.Vanilla Custard 300 THB",amount,amount*300,"THB")
    else:
        print("There is no item in your selection")
else:
    print("ERROR")
print("Thank you for using the service")
print("--ADMIN LOGIN VERIFICATION--")

user = input("Enter your username: ")
if user == "admin":
    pswd = input("Enter your password: ")
    if pswd == "admin123":
        print("Verification Completed...100%")
        print("PLEASE LOGIN!")
    else:
        print("PASSWORD WRONG")
else:
    print("Verification Completed...100%")
    print("⚠️You can't Login")

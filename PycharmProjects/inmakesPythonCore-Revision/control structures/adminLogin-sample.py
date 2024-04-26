# admin login details
admin=input("Enter admin name:")
password=int(input("enter 4 digit admin password:"))

# login verification
if admin == "admin" and password == 0000:
    print("Verification success!")
else:
    print("invalid credentials")
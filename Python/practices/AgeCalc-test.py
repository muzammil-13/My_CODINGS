"""
AGE CALCULATOR
"""

print("!CAUTION: Enter every input in numbers!")

# entering birthdate details
print("PLEASE ENTER BIRTH DATE DETAILS BELOW,")
b_day = int(input("Enter day: "))
b_month = int(input("Enter month: "))
b_year = int(input("Enter year: "))

# entering current date details
print("PLEASE ENTER CURRENT DATE BELOW,")
c_day = int(input("Enter current day: "))
c_month = int(input("Enter current month: "))
c_year = int(input("Enter current year:"))


# difference of current date and birthdate

age_y = c_year - b_year # year

if c_month >= b_month: # month
    age_m = c_month - b_month
else:
    age_m=b_month-c_month

age_d = c_day - b_day # day

print(f"Your age is: {age_y} years, {age_m} months and {age_d} days")

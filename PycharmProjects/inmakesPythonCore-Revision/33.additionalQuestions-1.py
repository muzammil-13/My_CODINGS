"""
1) print 1 to 12th calendar month when entering number 1 to 12 accordingly. Also print "Invalid: if user enters
incorrect number.
"""
cal = int(input("Enter the calendar month in digits: "))
print("Selected Month is",end=" ")
if cal == 1:
    print("January")
elif cal == 2:
    print("February")
elif cal == 3:
    print("March")
elif cal == 4:
    print("April")
elif cal == 5:
    print("May")
elif cal == 6:
    print("June")
elif cal == 7:
    print("July")
elif cal == 8:
    print("August")
elif cal == 9:
    print("September")
elif cal == 10:
    print("October")
elif cal == 11:
    print("November")
elif cal == 12:
    print("December")
else:
    print("Invalid")

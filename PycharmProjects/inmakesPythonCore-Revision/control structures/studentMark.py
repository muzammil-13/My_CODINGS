mark = int(input("Enter the mark /100 :"))
if mark > 100:
    print("marks input the exceeded the limit \"out of 100\"")
elif mark >= 90:
    print("A+ grade")
elif mark >= 80:
    print("A grade")
elif mark >= 70:
    print("B+ grade")
elif mark >= 60:
    print("B grade")
elif mark >= 50:
    print("C+ grade")
elif mark >= 40:
    print("C grade")
else:
    print("FAILED")

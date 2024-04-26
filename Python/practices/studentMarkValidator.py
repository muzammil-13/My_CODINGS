mark=int(input("Enter the student's marks:\n"))
print(f"STUDENT MARK is {mark} which is",end=" ")
if mark>=90:
    print("an A grade")
elif mark>=80:
    print("a B grade")
elif mark>=70:
    print("a C grade")
elif mark>=60:
    print("a D grade")
else:
    print("FAILED!!")
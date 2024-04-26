x = int(input("enter first number:\n"))
y = int(input("enter second number:\n"))

print(f"User entered values:\nx={x}\ny={y}")
print("by validating both numbers,")
if x < y:
    print(f"{x} (value of x) is less than {y} (value of y)")
elif x == y:
    print(f"{x} (value of x) and {y}  (value of y) are equal")
else:
    print(f"{y} (value of y) is less than {x}  (value of x)")

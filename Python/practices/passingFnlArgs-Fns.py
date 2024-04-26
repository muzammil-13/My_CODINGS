try:
    a = input("Enter the first number:")
    a = int(a)
except ValueError:
    print("⚠️ Enter only integers ⚠️")
    a = 0

try:
    b = input("enter the second number:")
    b = int(b)
except ValueError:
    print("⚠️ Enter only integers ⚠️")
    b = 0


def add(a, b):
    return a + b


def square(c):
    return c * c


print("Square value of the sum of two numbers: ", square(add(a, b)))

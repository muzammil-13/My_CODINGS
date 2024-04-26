"""
Write a function which would divide two numbers, design the
function in a manner that it handles the divide by zero exception
"""


def div(a, b):
    try:
        result = a / b
        print("Answer is ", result)
    except:
        print("Zero division found")


x = int(input("Enter value for a: "))
y = int(input("enter value for b: "))
div(x, y)

"""
Create a function , and calculated using the formula:
Final Price(FP) = (Product Price of X )/(Product Price of Y)^2.
Write python code which can accept the price X and price of Y of a
Product and calculate the FP. Note: Make sure to use a function
which accepts the X and Y values and returns the FP value
"""


def value(x, y):
    fp = x / y ** 2
    return fp


x = int(input("Product price of X: "))
y = int(input("Product price of Y: "))
result = value(x, y)
print("Final Price= ", result)

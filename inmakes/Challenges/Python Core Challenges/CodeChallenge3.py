def fn(x,y):
    fp=x/y**2
    return fp

x=float(input("enter the price of X:"))
y=float(input("enter the price of y:"))

result=fn(x,y)
print("Final price is=",result)
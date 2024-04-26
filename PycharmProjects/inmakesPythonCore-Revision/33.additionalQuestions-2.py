"""
2) Find simple interest, using Function:
Equation: (p*n*r)/100
p= principal amount
n= loan period
r= rate of interest
"""


def simple_interest(p, n, r):
    return (p * n * r) / 100


p = int(input("Enter principal amount: "))
n = int(input("Enter loan period (years): "))
r = int(input("Enter rate of interest: "))

result=simple_interest(p,n,r)
print("simple interest= ",result)
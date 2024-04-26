# 2.find simple interest, using function.
# equation= (p*n*r)/100
def si(p,n,r):
     return (p*n*r)/100
p=float(input("Enter the amount:"))
n=float(input("Enter the loan period (in years):"))
r=float(input("Enter the rate of interest:"))
print("Your interest is=",(p*n*r)/100)

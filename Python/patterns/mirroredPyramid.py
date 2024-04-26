"""
    1
   12
  123
 1234
12345
"""
r=6
for r in range(1,r):
    num=1
    for j in range(r,0,-1):
        if j>r:
            print(" ",end=" ")
        else:
            print(num,end="")
            num+=1
    print(" ")

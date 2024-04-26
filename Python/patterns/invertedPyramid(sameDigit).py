"""
55555
5555
555
55
5
"""

r=5
n=r
for i in range(r,0,-1):
    for j in range(0,i):
        print(n,end="")
    print('\r')

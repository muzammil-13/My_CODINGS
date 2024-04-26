"""
1
21
321
4321
54321
"""
rows=6
for r in range(1,rows):
    for c in range(r,0,-1):
        print(c,end=" ")
    print(" ")

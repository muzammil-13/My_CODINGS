"""
1
12
123
1234
12345
"""

rows=5
for row in range(1,rows+1):
    for c in range(1,row+1):
        print(c,end="")
    print("")
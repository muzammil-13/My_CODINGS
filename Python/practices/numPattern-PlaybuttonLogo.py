#print number sequence
a=range(1,10)
for i in a:
    print(*range(1,i+1))

#print number sequence reversely
b=range(10,1,-1)
for i in b:
    print(*range(1,i+1))
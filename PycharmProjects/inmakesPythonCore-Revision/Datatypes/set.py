# set sample
num = {10, 20, 30}
print(type(num))
print(num)

# adding a value to the set
num.add(12)
print(num)

# removing a value
num.remove(10)
print(num)

# set Operations
setA = {10, 20, 30}
setB = {30, 40, 50}

print(setA | setB)  # union operator used

print(setA & setB)  # Intersect (AND) operator

print(setA - setB)  # difference operator

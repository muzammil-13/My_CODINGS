x = (1, 2, 3, "hello", "world", "python")
print(type(x))

# converting tuple into list
y = list(x)
print(type(y))

print("tuple =",x)
print("list =",y)

y.insert(3,"Nice")
print(y)

# reconverting list into tuple
x=tuple(y)
print(type(x))
print(x)

# tuple using constructor
y=tuple((123,"helloi","hey"))
print(y)

# tuple through for loop
print("For loop,")
x=(12,13,"hello","python")
for i in x:
    print(i)

# joining 2 tuples
x=(12,13,"hello","python")
y=("&",2,3,5)
print(x+y)

# print multiple times
x=(12,13,"hello","python","&")
y=x*3
print(y)

x={
    "chair":500,
    "table":1000,
    1:"python",
    # "table":200,
}
print(len(x))
print(x["table"])
x["apple"]=100
print(x)
x.update({123:"django"})
x.pop("table")
print(x)

#show only keys
print("keys of x,")
for i in x:
    print(i)

#show values of the keys,
print("values of x,")
for i in x.values():
    print(i)

# show both keys & values from a specified variable
for i in x.items():
    print(i)

# dictionary function
print("Dictionary function,")
numbers={
    1:"one",
    2:"two",
    3:"three",
}
print(numbers.get(1,"key not found!"))
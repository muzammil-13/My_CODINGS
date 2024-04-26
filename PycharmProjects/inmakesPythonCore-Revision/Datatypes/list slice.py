# wrapping data from a list is the "List slice"
x = [10, 20, 30, 40, 50, 60, 70]
print(x)
print([x[1:5]])  # print index 1 to 5 elements of x

print(x[:8])  # prints from index beginning to 7th index

print(x[3:])  # print from 3rd index to end index

print(x[1:8:2]) # print from index 1 to 8 with intervals of 2

example = [1, 2, 3, 4, 5]
print("List for slicing:", example)

try:
    a = int(input(f"Enter a given value to start the slice: "))
    b = int(input(f"Enter a given value which ends the slice: "))
    if a<0 or b<0 or a>len(example) or b>len(example):
        raise ValueError("Invalid input. Enter from within the range")

    print("After slicing: ", example[a:b+1])
except ValueError as e:
    print(e)

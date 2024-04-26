try:
    input1 = int(input("pass any integer variable:"))
except ValueError:
    print("!! ENTER ONLY INTEGERS !!")
    input1 = 0  # default value

input2 = input("pass any string variable:")
a = input1
b = input2
print("memory address of integer variable a is: ", id(a))
print("memory address of string variable a is: ", id(b))

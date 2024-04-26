input_str = input("Enter numbers [*must be separated by spaces] :")

input_str_list = input_str.split()

input_int_list = [int(x) for x in input_str_list]

print("The list of inputted INTEGERS are:", input_int_list)
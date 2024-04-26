print("✂ DUPLICATE ARRAY ELEMENTS REMOVER ⚡")

arr = input("Enter numbers [*must be separated by spaces] :")
input_str_list = arr.split()
input_int_list = [int(x) for x in input_str_list]
print("The list of inputted INTEGERS are:", input_int_list)


def remove_duplicates(input_int_list):
    unique_elements = set()

    for element in input_int_list:
        if element not in unique_elements:
            unique_elements.add(element)
    return list(unique_elements)


unique_arr = remove_duplicates(input_int_list)
print(f"Original array: {input_int_list} \n Now duplicates are being filtered\n......%")
print(".....1%")
print("....99%")
print(f"Array after removing duplicates: {unique_arr}")

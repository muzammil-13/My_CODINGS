string=input("enter your string: ")
array=string

def remove_duplicates(array):
    unique_elements=set()
    for element in array:
        if element not in unique_elements:
            unique_elements.add(element)
    return list(unique_elements)

unique_array=remove_duplicates(array)
print(f"original array: {array}")
print(f"after removing duplicate: {unique_array}")

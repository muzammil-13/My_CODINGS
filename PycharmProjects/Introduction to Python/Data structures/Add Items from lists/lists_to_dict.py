list_of_keys = ["key1", "key2", "key3"]
list_of_values = [100, 200, 300]

my_dict = {}
for x in range(len(list_of_keys)):
    my_dict[list_of_keys[x]] = list_of_values[x]
    # TODO: populate the dictionary with key:value pairs from the lists

print(my_dict.items())

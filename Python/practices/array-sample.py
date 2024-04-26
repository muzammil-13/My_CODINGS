import array as arr

my_array=arr.array('i',[1,2,3,5,6])
print(f"Array elements are [",*my_array,"]")
print("and its type is",type(my_array))
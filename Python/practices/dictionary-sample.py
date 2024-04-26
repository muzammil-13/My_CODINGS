dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']:", dict['Name'])
print("dict['Age']:", dict['Age'])
print("dict['Class']", dict['Class'])

# modification
dict['Name']='Noora'
dict['Age']=8
dict['School']="AKJM School"

print("Updated Dictionary: \n",dict)
print("Total length of the dictionary is ",len(dict))
print("String representation: ",str(dict))
print("Passed variables are from ",type(dict))

# deletion
del dict['Name']
print("Name entry key deleted!\n",dict)

dict.clear()
print("Here,\nAll entries cleared",dict)

del dict;
print("And here,\ndeleted entire dictionary")
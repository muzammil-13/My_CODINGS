fruits=["Apple","Orange","Mango","Grapes"]

# list append
fruits.append("pineapple")
print("after list append: ",fruits)

# list insert
fruits.insert(2,"jack fruit")
print("after list insert: ",fruits)

# list length
print("list length is ",len(fruits))

# list index
print("mango's index is ",fruits.index("Mango"))

# list remove
fruits.remove("Grapes")
print("after removing grapes, the list is "+str(fruits))
# list comprehension
name = [i for i in "Muzammil"]
print(name)

# using sample Search method
searchList = ["python", "django", "people", "flask"]
searchKey = input("Enter the letter for searching:")
searchResult = [i for i in searchList if searchKey in i] # searching for element in the list
print(f"Search Result={searchResult}")

# printing List using Range
listRange = [i for i in range(10)]
print(listRange)

# printing an expression
exp = ["inmakes" for i in searchList]  # "inmakes" is the expression here.
print(exp)  # prints by replacing all elements in "result" with expression, ie: "inmakes"

# printing upper cases
ListUpper=[i.upper() for i in searchList]
print(ListUpper)

# printing calculated digits in List
num=[1,2,3,4]
calDigits=[i*i for i in num]
print(calDigits)
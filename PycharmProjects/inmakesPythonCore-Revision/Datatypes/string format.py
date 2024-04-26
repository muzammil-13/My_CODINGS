# using .format method
list1 = [10, 20, 30, 40, 50]
newstring = "My numbers: {0},{1},{2}".format(list1[0], list1[1], list1[3])
print(newstring)

# using Modulo operator
print("i'm learning %s, im using Pycharm IDE" % 'python')  # single string formatting

print("Im learning %s, Im using %s IDE" % ('python', 'pycharm'))  # multiple string formatting

print("You have been credited with %f on your %s account" % (1000, "SBI"))  # float + string value formatting

print("You have been credited with %3.2f on your %s account" % (
1000, "SBI"))  # sets precision length on float + string value formatting

perNum = int(input("Enter your phone number: "))  # input method string format with integer value
print("My phone number is %d" % perNum)

# string functions
upString="Hello im Muzammil" # printing in Uppercase
print(upString.upper())

lowString="Hello im MUZAMMIL" # printing in lowercase
print(lowString.lower())

checkString="Hello there how are you" # to check the letter in String
print(checkString)
checkKey1=input("Enter starts with keyword:")
print(checkString.startswith(checkKey1))
checkKey2=input("Enter ends with keyword:")
print(checkString.endswith(checkKey2))

#Numeric function
print("Minimum value=",min(2,5,6,8)) # minimum value in the list

print("Maximum value=",max(1,2,3,4)) #maximum value in the list

print("Absolute value=",abs(-123)) # finding absolute value



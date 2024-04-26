def reverse(string):
    result=""
    for i in string:
        result=i+result
    return result


string=input("enter a string to reverse: ")
print("Entered string: ",string)
print("Reversed string: ",reverse(string))

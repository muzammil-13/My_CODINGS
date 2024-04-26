while True:
    # error handling
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("OOPS! That was not a valid number. Try again!!!")

print("User entered number is: ", num)

# print ordered number or random number sequence chosen by user
print("Sequence available,\n option A: ordered | option B: random")

option = input("Enter your option:\n").lower()  # Convert input to lowercase for consistency

def option_choice(option):
    if option == "a":
        print("You chose an ordered number sequence.\n*This generates a number range automatically.")
        option_A()

    elif option == "b":
        print("You chose a random number sequence.\n*This requires manual entering.")
        option_B()

    else:
        print("Wrong option given. Please choose 'A' or 'B'.")

def option_A():
    try:
        n = int(input("Enter the start:"))  # Convert input to integer
        limit = int(input("Enter the limit:"))  # Convert input to integer
        for i in range(n, limit + 1):  # Add 1 to include the limit in the range
            print(i)
    except ValueError:
        print("Invalid input. Please enter valid integers for the start and limit.")

def option_B():
    num = []
    try:
        nums = int(input("How many numbers will you enter?"))  # Ask for the count of numbers
        for i in range(nums):
            num.append(int(input(f"Enter number {i + 1}:")))  # Append entered numbers to the list
        print("Entered numbers:", num)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

option_choice(option)

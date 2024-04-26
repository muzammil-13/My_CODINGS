"""
HOSPITAL PATIENT'S DATA COLLECTION
"""
patient = input("Enter patients name: ")
age = int(input("Enter patient's age: "))
sex = input("M/F ?:\n")
if sex == "m":
    print("MALE")
    sex1 = "He"
elif sex=="f":
    print("FEMALE")
    sex1 = "She"
else:
    print("ERROR INPUT ON GENDER!\nPlease enter \"M or F\" ")

new = input("New patient ?\n[True/False]")
if new == "true":
    print(f"{sex1} is a new patient")
elif new == "false":
    print(f"FOUND IN DATABASE! {sex1} is an old patient")
else:
    print("ERROR INPUT!!!!!")

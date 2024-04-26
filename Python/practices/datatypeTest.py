data=input("Enter anything to find its Datatype: ")
print(f"User entered {data},and its Datatype is:")
"""
Data type finder!
"""
try:
    data=int(data)
    print("INTEGER")
except ValueError:

    try:
        data=float(data)
        print("FLOAT")
    except ValueError:

        try:
            data=str(data)
            print("String")
        except ValueError:
            print("Data type not found on Database")
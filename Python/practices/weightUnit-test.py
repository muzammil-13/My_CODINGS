"""
WEIGHT UNIT FINDER
"""
weight=int(input("Enter your weight: "))

unit=input("In which unit you want to Find?\n [KG or LBs]\n").upper()

if unit=="KG":
    wkg=(weight*0.45359237)
    print(f"Your actual weight is {wkg} Kgs")
elif unit=="LBS":
    wlb=(weight*2.20462262)
    print(f"Your actual weight is {wlb} Lbs")
else:
    print("!ERROR OUTPUT!")

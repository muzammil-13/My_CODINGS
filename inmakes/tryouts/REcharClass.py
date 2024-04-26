import re
pattern="[A-Z][0-9][a-z]"
if re.search(pattern,"P8u"):
    print("matched")
else:
    ("not matched")
import re
pattern="python"
if re.match(pattern,"python hello how are you"):
    print("matched!")
else:
    print("not matched!")
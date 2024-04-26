import re
str="hai inmakes, hello india"
pattern="hello"
new=re.sub(pattern,"inmakes",str)
print(new)
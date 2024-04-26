# write
file = open("sample-fileHandling.txt", "w")
file.write("Hello muzammil!")
file.write("\nThis is an example for your file written by 'file writing' ")
file.close()

# read
file = open("sample-fileHandling.txt", "r")
content = file.read()
print(content)
file.close()

# append
file = open("sample-fileHandling.txt", "a")
file.write("\nThis a new line comes from 'file appending")

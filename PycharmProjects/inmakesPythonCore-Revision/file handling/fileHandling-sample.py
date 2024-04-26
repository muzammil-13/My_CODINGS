# # creating a file
# file=open("sample.txt",'w')

# # writable file
file=open("sample.txt",'w')
file.write("This is the written text.")
file.close()

# appending text
file=open("sample.txt",'a')
file.write("This is a appended text.")

# readable file
file=open("sample.txt",'r')
# file.close()



content=file.read()
print(content)
file.close()

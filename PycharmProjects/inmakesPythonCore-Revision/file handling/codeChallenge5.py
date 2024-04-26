"""
Write Python code to open a file named Fileprogram.txt and write
some random data into it.
Open the file, read the contents and display them as output.
Write python code to add additional text to the existing file on a new
line without deleting the previous contents
"""

file = open("fileprogram.txt", 'w')
file.write("this is some random text")
file.close()

file = open("fileprogram.txt", 'a')
file.write("\nanother text on next line")
file.close()

file = open("fileprogram.txt", 'r')
content = file.read()
print(content)
file.close()

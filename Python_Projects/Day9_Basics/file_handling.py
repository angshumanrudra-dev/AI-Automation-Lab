# Why File Handling is Important .Right now your programs forget everything after closing.now it will be saved in file.
# This is the start of real automation systems.

# syntax
# file = open("filename.txt", "mode")

# Modes
# "r" → read
# "w" → write (overwrite)
# "a" → append (add data)

# file = open("test.txt", "r")
# content = file.read()
# print(content)
# file.close()

# TO WRITE IN THE FILE
file = open ("test.txt","w")
file.write ("Hello Python\n Automation is powerful \n")
file.close()

# TO READ FROM THE FILE
file = open("test.txt","r")
content=file.read()
print(content)
file.close()

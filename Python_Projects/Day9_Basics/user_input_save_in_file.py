user_name = input("Tell me your beautiful name: ")
file= open ("test.txt","w")
file.write(user_name+ "\n")
file.close()

file = open("test.txt","r")
content=file.read()
print(content)
file.close()

file = open("test.txt", "a")
file.write("New data\n")
file.close()


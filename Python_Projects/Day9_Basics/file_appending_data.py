#  My version
# user_name = input("Tell me your beautiful name: ")
# file= open ("test.txt","w")
# file.write(user_name+ "\n")
# file.close()
# i=0
# while i<2:
#     user_name2= input("Tell me your name?: ")
#     file = open("test.txt", "a")
#     file.write(user_name2+"\n")
#     file.close()
#     i=i+1

# file = open("test.txt","r")
# content=file.read()
# print(content)
# file.close()



# simplest version

# clear file once (optional)
open("test.txt", "w").close()

# take 3 inputs
for i in range(3):
    user_name = input("Enter name: ")

    with open("test.txt", "a") as file:
        file.write(user_name + "\n")

# read file
with open("test.txt", "r") as file:
    print(file.read())
# with open("test.txt","w") as file: #it  will open file.delete all content.leaves it empty
#     pass

# for i in range(6): #add new data
#     user_name = input("Enter name: ")

#     with open("test.txt", "a") as file:
#         file.write(user_name + "\n")

# read file
with open("test.txt", "r") as file:
    print(file.read())

#print
count =0
with open("test.txt", "r") as file:
    for line in file:
        name = line.strip()
        if name.startswith("s"):
         count = count+1
    print("count: ",count)
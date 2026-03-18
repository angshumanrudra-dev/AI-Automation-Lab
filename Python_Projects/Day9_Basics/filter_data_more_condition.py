with open("test.txt","w") as file: #it  will open file.delete all content.leaves it empty
    pass

for i in range(6):
    user_name = input("Enter name: ")

    with open("test.txt", "a") as file:
        file.write(user_name + "\n")

# read file
with open("test.txt", "r") as file:
    print(file.read())


with open("test.txt", "r") as file:
    for line in file:
        name = line.strip()
        name_length=len(name)
        if name.startswith("s") or name_length > 5:
           print(name)
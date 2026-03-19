# 🎯 Goal:

# 👉 Read data from file
# 👉 Clean it
# 👉 Extract useful info
# 👉 Apply logic
# 👉 Show result

### What my program is Doing #########
#  Input --- store --- read--- process---filter---count ----output
# clear file once (optional)
open("test2.txt", "w").close()

# take inputs
for i in range(3):
    user_name = input("Enter Email Id: ")

    with open("test2.txt", "a") as file:
        file.write(user_name + "\n")

# read file
with open("test2.txt", "r") as file:
     i=0
     count = 0
     count2 = 0
     print("Username with letter more than 5:")
     for line in file:
        count += 1
        
        email =line.strip()
        # len_email=len(email)
        # if len_email>5:
        #     print(email)
        if "@gmail.com" in email:
            count2 +=1
            
        #     print(email)
        email_split = email.split("@")
        # print("Username: ",email_split[0],"Domain: ",email_split[1])
        if len(email_split[0]) >5:
           print(email)
           i=i+1
     print("Total user:", count)
     print("Matched user: ",i)
     print("Gmail User: ",count2)
     
            
        # print(email_split)
        # print(email)
# contact_dict={}
# i=1
# while i <3:
#     name = input("what is your name? ")
#     contact_number = input ("your mobile number please?  ")
#     contact_dict[name]= contact_number
#     i=i+1
# print (contact_dict)

contact_dict = {}

for i in range(2):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact_dict[name] = phone

print(contact_dict)



contact_dict = {}

for i in range(3):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact_dict[name] = phone

print(contact_dict)

contact_search= input("what is the name of the person whose number you are searching? ")
if contact_search in contact_dict:
    print("Contact Number of", contact_search, "is: ", contact_dict[contact_search])
else:
    print("name not found")


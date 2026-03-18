email = input("tell me your email ID: ")
email_split = email.split("@")
print(email_split)

print("Username:", email_split[0])
print("Domain:", email_split[1])
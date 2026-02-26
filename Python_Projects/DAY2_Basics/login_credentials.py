username = input ("username: ")
password = input ("Password: ")

if username == "admin":
    if password == "1234":
        print ("Login successful")
    else:
        print ("wrong password")
else:
    print("Invalid username") 
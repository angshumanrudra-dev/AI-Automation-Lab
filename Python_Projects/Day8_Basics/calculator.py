def addition(a,b):
    return (a+b)

def substraction(a,b):
    return (a-b)

def multiply(a,b):
    return (a*b)

def division(a,b):
    return (a/b)
while True:
    num1= int(input("Tell me your first number: "))
    num2= int(input("Tell me your second number: "))

    action= input("which action do you want add/sub/mul/div ? ")

    if action == "add":
      print("Result= ",addition(num1,num2))
    elif action == "sub":
      print("result= ",substraction(num1,num2))
    elif action == "mul":
      print("Result=",multiply(num1,num2))
    elif action== "div":
      print("Result=",division(num1,num2))
    else:
      print("wrong input")

    prompt = input("Do you want to contine (yes/no): ")
    if prompt == "yes":
      continue
    if prompt == "no":
       break
    



num1 = int(input("tell me a number: "))
num2 = int(input("tell me second number: "))

input_1 = input ("choose operation among add/sub/multi/div : ")

if input_1 == "add" :
    add = num1 + num2
    print (f"Add : {add}")
elif input_1 == "sub":
    sub = num1 - num2
    print (f"sub: {sub}")
elif input_1 == "multi":
    multi = num1 * num2
    print (f"multi: {multi}")
elif input_1 == "div":
    if num2 == 0:
        print ("infinite number")
    else:
        div = num1/num2
        print (f"div:{div}")

    
    
    












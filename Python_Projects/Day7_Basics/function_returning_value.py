# Function Returning a Value
# A function returning a value means the function calculates 
# something and sends the result back to the place where it was called.
# It uses the keyword: return

# def function_name(parameters):
#     calculation
#     return value

# def test(a,b):
#     return (a+b)

# x=test(3,4)

# print(x)

def add(a,b):
    return int(a+b)

x= add(5,4)
print(x)

def multiply(a,b):
    return(a*b)
x= multiply(56, 10)
print(x)
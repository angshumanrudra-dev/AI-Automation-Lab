# A function can call another function.

def square(x):
    return x * x

def show_square(number):
    result = square(number)
    print(result)

show_square(6)
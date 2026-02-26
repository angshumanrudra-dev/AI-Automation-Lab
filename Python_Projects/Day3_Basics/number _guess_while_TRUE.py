secret_number = 88

while True:

    guess_number = int(input("Guess a number: "))

    if guess_number == secret_number:
        print("Right Guess")
        break
    else:
        print("Wrong Guess")
age = int(input("what is your age? "))


if age >= 21 :
    income = int(input("what is your monthly income ? "))
    if income >= 25000:
        credit_score = int(input ("what is your credit score ? "))
        if credit_score >= 650:
            print("Loan approved")
        else:
            print("credit score is low")
    else:
        print("income is low")
else:
    print("Not Eligible")
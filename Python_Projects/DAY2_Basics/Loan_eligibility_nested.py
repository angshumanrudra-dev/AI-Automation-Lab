age = int(input("what is your age? "))
if age < 21 :
    print("Not Eligible")
else:
    income = int(input("what is your monthly income ? "))
    if income < 25000:
        print("income is low")
    else:
        credit_score = int(input ("what is your credit score ? "))
        if credit_score < 650 :
            print("credit score is low")
        else:
            print("Loan approved")


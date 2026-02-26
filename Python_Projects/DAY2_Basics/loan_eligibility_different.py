age = int(input("what is your age? "))
income = int(input("what is your monthly income ? "))
credit_score = int(input ("what is your credit score ? "))
if age < 21 :
   print("Not Eligible")
elif income < 25000:
   print("income is low")
elif credit_score < 650:
   print("Credit score is low")
else :
   print ("Loan approved")

   
   
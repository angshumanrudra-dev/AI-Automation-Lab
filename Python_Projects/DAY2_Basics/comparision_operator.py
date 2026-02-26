"""
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater or equal
<=   less or equal
"""

age = int(input("what is your age ? : "))
if age < 0:
    print ("Invalid age")
elif age <18:
    print(" Not Eligible")
elif age >= 18 and age<= 60:
    print ("Eligible adult voter")
elif age > 60:
    print("Senior citizen voter")


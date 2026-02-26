"""
and   → both conditions must be True
or    → at least one must be True
not   → reverses the condition

"""

name = input("what is your name? ")
age = int(input(f"{name}, what is your age: "))
has_voter_id = input(f"{name}, Do you have voter id (Yes/No): ").lower

if age < 18:
    print("you are too young to vote")
elif age >= 18 and has_voter_id == "yes":
    print ("you are allowed to vote")
elif age >= 18 and has_voter_id == "no":
    print ("you need voter ID")

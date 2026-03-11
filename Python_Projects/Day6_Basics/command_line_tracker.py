expenses = []

while True:

    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        expense_name= input ("Enter expense name: ")
        expense_amount = int(input ("Enter expense amount: "))
        expense = {
            "name": expense_name , "amount":(expense_amount)
            }
        expenses.append(expense)

    elif choice =="2":
        print (f"your expenses")

        for expense in expenses:
            print(expense["name"],":", expense["amount"])

    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print(f"total Expenses : {total}")

    elif choice == "4":
        print("Exiting program..")
        break
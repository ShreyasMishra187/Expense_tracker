expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    
    expenses.append({"name": name, "amount": amount})
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    
    print("\nYour Expenses:")
    for expense in expenses:
        print(f"{expense['name']} - ₹{expense['amount']}")
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spending: ₹{total}\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        break
    else:
        print("Invalid choice\n")
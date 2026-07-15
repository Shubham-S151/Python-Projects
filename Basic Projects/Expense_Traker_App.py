"""
Project Name: Expense Tracker App

Description:
This is a simple command-line expense tracker built using Python.
The program allows users to add expenses, view all recorded expenses,
delete an expense, and see a summary of total spending along with
category-wise totals.

Each expense contains:
- Category
- Description
- Amount

All expenses are stored in a list where each item is a dictionary
representing a single expense.

Concepts Used:
- Variables
- Lists
- Dictionaries
- Functions
- Loops (while loop, for loop)
- Conditional statements (if, elif, else)
- User input using input()
- String formatting (f-strings)
- enumerate() function
- Built-in functions (sum, len)
- Basic input validation
"""

expenses = []

def add_expense():
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount  = float(input("Enter the amount: "))

    expense = {
        "category" : category,
        "description" : description,
        "amount" : amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expense():
    if not expenses:
        print("No Record Present!")
        return
    
    print("\n--- Expense List ---")
    print(f"{'Index':<10}{'Category':<15}{'Description':<25}Amount")
    print('-'*50)
    for i, exp in enumerate(expenses):
        print(f"{i:<10}{exp['category']:<15}{exp['description']:<25}{exp['amount']}")

def delete_expense():
    if not expenses:
        print("No Record Present!")
        return
    index = int(input("Enter the index to delete: "))

    if index < 0 or index > len(expenses):
        print("Invalid index!")
    
    expenses.pop(index)
    print("Expense deleted successfully!")

def show_summary():
    if not expenses:
        print("No expenses recorded.")
        return
    
    total = sum(exp["amount"] for exp in expenses)
    print("\nTotal Expenses:", total)
    print("\nCategory-wise Summary:")

    category_total = {}

    for exp in expenses:
        category = exp['category']
        amount = exp['amount']

        if category in category_total:
            category_total[category] += amount
        else :
            category_total[category] = amount

    for category, total in category_total.items():
        print(category, ":", total)

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")

        while True:
            choice = int(input("Enter choice: "))
            if choice <0 or choice >5 :
                print("Invalid Choice!")
            else :
                break
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            delete_expense()
        elif choice == 4:
            show_summary()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()
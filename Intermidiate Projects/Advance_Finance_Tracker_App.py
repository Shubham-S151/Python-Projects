"""
Project Name: Advanced Expense Tracker (CLI)

Description:
A command-line based expense tracker that allows users to manage daily expenses efficiently.
The application supports adding, viewing, deleting, searching, and filtering expenses,
along with budget tracking and persistent data storage using JSON.

---

File Structure Overview:

1. Imports

   * json → for saving/loading data
   * datetime → for timestamping expenses

2. Constants

   * FILE_NAME → stores the JSON file name

3. File Handling Functions

   * load_data() → loads expenses and budget from file
   * save_data() → saves expenses and budget to file

4. Core Features

   * add_expense() → adds a new expense with date & time
   * view_expenses() → displays all stored expenses
   * delete_expense() → removes an expense by index

5. Summary & Analysis

   * show_summary() → shows total and category-wise spending
   * budget check → compares total expenses with set budget

6. Search & Filter Features

   * search_by_category() → finds expenses by category
   * filter_recent() → shows expenses from last N days

7. Budget Management

   * set_budget() → allows user to define monthly budget

8. Main Control Flow

   * main() → menu-driven interface using while loop
   * handles user input and calls appropriate functions

---

Concepts Used:

* Functions (modular programming)
* Lists & Dictionaries (data storage)
* File Handling (JSON read/write)
* Exception Handling (try-except)
* Loops (while, for)
* Conditional Statements (if-else)
* Date & Time handling
* Input validation
* Data persistence

---
"""


import json
from datetime import datetime

"""{"budget": 10000,
    "expenses": [
    {"category": "Food",
    "description": "Lunch at restaurant",
    "amount": 250.5,
    "date": "2026-04-05 14:30"},

    {"category": "Transport",
    "description": "Auto fare",
    "amount": 80,
    "date": "2026-04-05 10:15"}
    ]
}
"""

FILE_NAME = "finance_expenses.json"

# ------------------ FILE HANDLING ------------------ #
def load_data():
    try:
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            return data.get("expenses",[]), data.get("budget", 0)
    except FileNotFoundError:
        return [],0

def save_data(expenses, budget):
    data = {"expenses":expenses,
            "budget": budget}
    with open(FILE_NAME,"w") as file:
        json.dump(data,file,indent=4)

# ------------------ CORE FEATURES ------------------ #
def add_expense(expenses, budget):
    category = input("Enter your category: ")
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid Amount!")
        return expenses, budget
    
    expense = {
        "category": category,
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    expenses.append(expense)
    save_data(expenses,budget)
    print("Expense Added!")
    return expenses, budget

def view_expenses(expenses):
    if not expenses:
        print("No Expenses found!")
        return 
    
    print("\n------------Expenses------------")
    print(f"{'Index':<6}{'Category':<15}{'Amount':<10}{'Date':<20}Description")
    print("-" * 65)

    for i, exp in enumerate(expenses):
        print(f"{i:<6}{exp['category']:<15}₹{exp['amount']:<10}{exp['date']:<20}{exp['description']}")

def delete_expense(expenses, budget):
    if not expenses:
        print("No expenses to delete!")
        return expenses, budget
    
    view_expenses(expenses)

    try :
        index = int(input("Enter the index to delete: "))
        if index<0 or index >=len(expenses):
            print("Invalid index!")
            return expenses, budget
    except ValueError:
        print("Invalid Input!")
        return expenses, budget
    
    expenses.pop(index)
    save_data(expenses,budget)
    print("Expense deleted successfully!")
    return expenses, budget
    
# ------------------ SUMMARY ------------------ #
def show_summary(expenses, budget):
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spending: ₹{total}")

    print("\nCategory-wise Breakdown:")
    category_total = {}

    for exp in expenses:
        category = exp["category"]
        category_total[category] = category_total.get(category, 0) + exp["amount"]

    for cat, amt in category_total.items():
        print(f"{cat}: ₹{amt}")

    if budget > 0:
        print(f"\nBudget: ₹{budget}")
        if total > budget:
            print("Budget exceeded!")
        else:
            print(f"Remaining: ₹{budget - total}")

# ------------------ SEARCH & FILTER ------------------ #
def search_by_category(expenses):
    cat = input("Enter the category to search: ")
    found = False

    for exp in expenses:
        if exp['category'].lower() == cat.lower():
            print(exp)
            found = True
    
    if not found:
        print("No matching record found!")

def filter_recent(expenses):
    try:
        days = int(input("Enter the number of days: "))
    except ValueError:
        print("Invalid Input!")
        return 
    
    now = datetime.now()
    print(f"\nExpenses from last {days} days:\n")

    found = False
    for exp in expenses:
        exp_date = datetime.strptime(exp["date"], "%Y-%m-%d %H:%M")
        if (now-exp_date).days <= days:
            print(exp) 
            found = True
    
    if not found:
        print("No expenses found!")

# ------------------ BUDGET ------------------ #
def set_budget(expenses, budget):
    try:
        budget = float(input("Enter monthly budget: "))
        save_data(expenses, budget)
        print("Budget set!")
    except ValueError:
        print("Invalid Amount!")
    return expenses, budget

# ------------------ MAIN PROGRAM ------------------ #
def main():
    expenses, budget = load_data()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Search by Category")
        print("6. Filter by Recent Days")
        print("7. Set Budget")
        print("8. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if choice == 1:
            expenses, budget = add_expense(expenses, budget)
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            expenses, budget = delete_expense(expenses, budget)
        elif choice == 4:
            show_summary(expenses, budget)
        elif choice == 5:
            search_by_category(expenses)
        elif choice == 6:
            filter_recent(expenses)
        elif choice == 7:
            expenses, budget = set_budget(expenses, budget)
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()
import json
import os

# The list hold the expense in memory whule program run
expenses = []

# 1 add_expense
def add_expense():
    print("\n -------- Add a New Expense --------")
    amount = float(input("Enter the amount of spent: Rs"))
    description = input("Enter a brief description: ").strip().title()
    category = input("Enter category (e.g., food, travel, entertainment): ").strip().title()
    
    # now we create dictionary for new expense
    new_expense = {
        "amount" : amount,
        "description" : description,
        "category" : category
    }

    # add the new expense dictionary to our list 
    expenses.append(new_expense)
    print("✅ Expense added successfully!")

# 2 view_expenses
def view_expense():
    print("\n -------- All Expense --------")
    if not expenses: #check it list is empty
        print("No expense recorded yet")
        return

    #loop through the list and print each expense
    for i, expense in enumerate(expenses, start = 1):
        print(f"{i}. Rs{expense['amount']} - {expense['description']} ({expense['category']})")

# 3 view_summary
def view_summary():
    print("\n -------- Expense Summary --------")
    if not expenses:
        print("No expense summarize")
        return
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Amount spent: Rs{total : 2f}")

# 4 save_expenses
def save_expenses():
    with open('expense.txt', 'w') as file:
        # convert file into json
        json.dump(expenses, file)
        print("Data saved.")

# 5 load_expenses
def load_expenses():

# This tells the function to use the global 'expenses' list we created at the top
    global expenses 
    if os.path.exists('expenses.txt '):
        try:
            with open('expenses.txt', 'r') as file:
                expenses = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            # If the file is empty or corrupted, start with a fresh list
            expenses = []

    #If the file doesn't exist, just keep the empty list
    else:
        expenses = []        

# 6 
def main():
    load_expenses()
    while True:
        print("\n" + "=" * 40 )
        print("Rs Personal Expense Tracker")
        print("=" * 40)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Save & Exit")

        choice = input("\n Enter your choice (1-4): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_expenses()
            print("📝 Data Saved.")
            break
        else: 
            print("Invalid choice! Re-Enter your choice again from number (1-4)")
if __name__ == "__main__":
    main()
import json
import os

# The list hold the expense in memory whule program run
expense = []

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


def view_expense():
    print("\n -------- All Expense --------")
    if not expenses: #check it list is empty
        print("No expense recorded yet")
        return

    #loop through the list and print each expense
    for i, expense in enumurate(expenses, start = 1):
        print(f"{i}. Rs{expense['amount']} - {expense['description']} ({expense['category']})")

def view_summary():
    print("\n -------- Expense Summary --------")
    if not expenses:
        print("No expense summarize")
        return
    total = sum(expense['amount'] for expense in expenses)
    pass


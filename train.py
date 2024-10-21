import csv
import os
from datetime import datetime

# Constants
FILE_NAME = 'expenses.csv'
CATEGORIES = ['Food', 'Transportation', 'Entertainment', 'Other']

# Ensure the file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Amount', 'Category', 'Description'])


def add_expense(amount, category, description):
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d'), amount, category, description])


def view_expenses():
    expenses = []
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return expenses


def summarize_expenses():
    expenses = view_expenses()
    monthly_summary = {}
    category_summary = {category: 0 for category in CATEGORIES}

    for expense in expenses:
        date = expense['Date'][:7]  # Get the YYYY-MM part of the date
        amount = float(expense['Amount'])
        category = expense['Category']

        # Monthly summary
        if date not in monthly_summary:
            monthly_summary[date] = 0
        monthly_summary[date] += amount

        # Category summary
        if category in category_summary:
            category_summary[category] += amount
        else:
            category_summary['Other'] += amount

    return monthly_summary, category_summary


def user_interface():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input(f"Enter category ({', '.join(CATEGORIES)}): ")
                if category not in CATEGORIES:
                    category = 'Other'
                description = input("Enter description: ")
                add_expense(amount, category, description)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '2':
            expenses = view_expenses()
            if expenses:
                print("\nDate\t\tAmount\tCategory\tDescription")
                for expense in expenses:
                    print(f"{expense['Date']}\t{expense['Amount']}\t{expense['Category']}\t{expense['Description']}")
            else:
                print("No expenses found.")

        elif choice == '3':
            monthly_summary, category_summary = summarize_expenses()
            print("\nMonthly Summary:")
            for month, total in monthly_summary.items():
                print(f"{month}: ${total:.2f}")

            print("\nCategory Summary:")
            for category, total in category_summary.items():
                print(f"{category}: ${total:.2f}")

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the user interface
if __name__ == "__main__":
    user_interface()

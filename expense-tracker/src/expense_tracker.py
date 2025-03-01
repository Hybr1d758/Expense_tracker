# filepath: /expense-tracker/expense-tracker/src/expense_tracker.py

import sys
from controllers.expense_controller import ExpenseController
from views.expense_view import display_expenses, display_summary

def main():
    controller = ExpenseController()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. View Expenses")
        print("5. View Summary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            controller.add_expense(description, amount)
            print("Expense added.")
        
        elif choice == '2':
            expense_id = int(input("Enter expense ID to update: "))
            description = input("Enter new expense description: ")
            amount = float(input("Enter new expense amount: "))
            controller.update_expense(expense_id, description, amount)
            print("Expense updated.")
        
        elif choice == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            controller.delete_expense(expense_id)
            print("Expense deleted.")
        
        elif choice == '4':
            expenses = controller.get_expenses()
            display_expenses(expenses)
        
        elif choice == '5':
            summary = controller.get_summary()
            display_summary(summary)
        
        elif choice == '6':
            print("Exiting the Expense Tracker.")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
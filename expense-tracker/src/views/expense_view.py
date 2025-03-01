def display_expenses(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    print("Expenses:")
    for expense in expenses:
        print(f"Description: {expense['description']}, Amount: {expense['amount']}, Date: {expense['date']}")

def display_summary(total_expenses, monthly_expenses):
    print(f"Total Expenses: {total_expenses}")
    print("Monthly Expenses:")
    for month, amount in monthly_expenses.items():
        print(f"{month}: {amount}")

def prompt_for_expense_details():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter expense date (YYYY-MM-DD): ")
    return {"description": description, "amount": amount, "date": date}
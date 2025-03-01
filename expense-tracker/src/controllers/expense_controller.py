class ExpenseController:
    def __init__(self, expense_model):
        self.expense_model = expense_model

    def add_expense(self, description, amount):
        expense = self.expense_model(description, amount)
        return expense.save()

    def update_expense(self, expense_id, description=None, amount=None):
        expense = self.expense_model.find_by_id(expense_id)
        if expense:
            if description:
                expense.description = description
            if amount:
                expense.amount = amount
            return expense.save()
        return None

    def delete_expense(self, expense_id):
        expense = self.expense_model.find_by_id(expense_id)
        if expense:
            return expense.delete()
        return None

    def get_expenses(self):
        return self.expense_model.get_all()

    def get_monthly_summary(self, month, year):
        expenses = self.expense_model.get_by_month(month, year)
        total = sum(expense.amount for expense in expenses)
        return total, expenses
class Expense:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date

    def validate(self):
        if not isinstance(self.amount, (int, float)) or self.amount < 0:
            raise ValueError("Amount must be a non-negative number.")
        if not isinstance(self.description, str) or not self.description:
            raise ValueError("Description must be a non-empty string.")

    def format_expense(self):
        return f"{self.date}: {self.description} - ${self.amount:.2f}"
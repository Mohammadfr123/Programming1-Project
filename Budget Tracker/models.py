class Transaction:
    def __init__(self, date, amount, category, description, ttype):
        # store fields; amount saved as float
        self.date = date               # string like "2025-10-15"
        self.amount = float(amount)    # convert to float for math
        self.category = category.lower().strip()  # normalize category
        self.description = description
        self.type = ttype              # "income" or "expense"

    def __str__(self):
        # string used when printing a transaction
        # e.g. "2025-10-15 | income  | salary     | 5000.00 | October salary"
        return f"{self.date} | {self.type:<7} | {self.category:<10} | {self.amount:8.2f} | {self.description}"

# Income subclass: same as Transaction but always type 'income'
class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "income")

# Expense subclass: same but type 'expense'
class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "expense")
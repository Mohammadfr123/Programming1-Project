# tracker.py
# BudgetTracker stores transactions and has methods to add, list, filter, and show summary.

from models import Income, Expense, Transaction

class BudgetTracker:
    def __init__(self):
        self.transactions = []  # list to keep Transaction objects

    # add a transaction object (Income or Expense)
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    # convenience methods for adding income or expense by data values
    def add_income(self, date, amount, category, description):
        inc = Income(date, amount, category, description)
        self.add_transaction(inc)

    def add_expense(self, date, amount, category, description):
        exp = Expense(date, amount, category, description)
        self.add_transaction(exp)

    # list all transactions in a readable format
    def list_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print("Date       | Type    | Category   |   Amount | Description")
        print("-" * 60)
        for t in self.transactions:
            print(t)

    # filter by type ('income'/'expense'), category (string), or month ('YYYY-MM')
    def filter_transactions(self, by, value):
        value = value.lower().strip()
        if by == "type":
            filtered = [t for t in self.transactions if t.type == value]
        elif by == "category":
            filtered = [t for t in self.transactions if t.category == value]
        elif by == "month":
            # assume date starts with YYYY-MM
            filtered = [t for t in self.transactions if t.date.startswith(value)]
        else:
            print("Unknown filter. Use 'type', 'category' or 'month'.")
            return

        if not filtered:
            print("No transactions match that filter.")
            return

        print("Date       | Type    | Category   |   Amount | Description")
        print("-" * 60)
        for t in filtered:
            print(t)

    # show totals: total income, total expenses, balance, and per-category totals
    def show_summary(self):
        total_income = sum(t.amount for t in self.transactions if t.type == "income")
        total_expense = sum(t.amount for t in self.transactions if t.type == "expense")
        balance = total_income - total_expense

        # per-category totals (income adds, expense subtracts)
        category_totals = {}
        for t in self.transactions:
            # start at 0 if not present
            category_totals.setdefault(t.category, 0)
            if t.type == "income":
                category_totals[t.category] += t.amount
            else:
                category_totals[t.category] -= t.amount

        print("===== Budget Summary =====")
        print(f"Total Income : {total_income:.2f}")
        print(f"Total Expense: {total_expense:.2f}")
        print(f"Balance      : {balance:.2f}")
        print("\nPer-category totals (positive = net income, negative = net expense):")
        for cat, amt in category_totals.items():
            print(f"  {cat:<10} : {amt:.2f}")
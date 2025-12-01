# main.py
# Simple command-line menu to interact with BudgetTracker

from tracker import BudgetTracker

def get_nonempty(prompt):
    # helper to ensure user types something
    while True:
        x = input(prompt).strip()
        if x:
            return x
        print("Please enter a value.")

def get_amount(prompt):
    # helper to ensure amount is numeric and positive
    while True:
        s = input(prompt).strip()
        try:
            value = float(s)
            if value < 0:
                print("Amount must be non-negative.")
                continue
            return value
        except ValueError:
            print("Enter a valid number (e.g., 500 or 12.50).")

def main():
    tracker = BudgetTracker()

    while True:
        print("Welcome to Mfr Budget Tracker!")
        print("\n--- Budget Tracker Menu (Enter your choice) ---")
        print("1) Add income")
        print("2) Add expense")
        print("3) List transactions")
        print("4) Filter transactions")
        print("5) Show summary")
        print("0) Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            date = get_nonempty("Enter date (YYYY-MM-DD): ")
            amount = get_amount("Enter amount: ")
            category = get_nonempty("Enter category: ")
            description = input("Enter description (optional): ")
            # add income (note we pass amount as number)
            tracker.add_income(date, amount, category, description)
            print("Income added.")

        elif choice == "2":
            date = get_nonempty("Enter date (YYYY-MM-DD): ")
            amount = get_amount("Enter amount: ")
            category = get_nonempty("Enter category: ")
            description = input("Enter description (optional): ")
            tracker.add_expense(date, amount, category, description)
            print("Expense added.")

        elif choice == "3":
            tracker.list_transactions()

        elif choice == "4":
            print("Filter by: type  (income/expense), category (e.g., food), or month (YYYY-MM)")
            by = get_nonempty("Enter filter type (type/category/month): ").lower()
            value = get_nonempty("Enter filter value: ")
            tracker.filter_transactions(by, value)

        elif choice == "5":
            tracker.show_summary()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

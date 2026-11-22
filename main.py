
from manager import TransactionManager
from reports import ReportManager
from budget import BudgetManager
from exporter import CSVExporter

manager = TransactionManager()
report_manager = ReportManager(manager.transactions)
budget_manager = BudgetManager(manager.transactions)
csv_exporter = CSVExporter()

def add_transaction():
    print("\n===== ADD TRANSACTION =====")

    try:
        transaction_type = input("Enter type (Income/Expense): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (DD-MM-YYYY): ")

        manager.add_transaction(
            transaction_type, amount, category, description, date
        )

    except ValueError:
        print("Invalid amount. Please enter a number.")


def view_transactions():
    print("\n===== ALL TRANSACTIONS =====")
    manager.view_all_transaction()

def update_transaction():
    print("\n===== UPDATE TRANSACTION =====")

    try:
        transaction_id = int(input("Enter transaction ID: "))
        transaction_type = input("Enter new type (Income/Expense): ")
        amount = float(input("Enter new amount: "))
        category = input("Enter new category: ")
        description = input("Enter new description: ")
        date = input("Enter new date (DD-MM-YYYY): ")

        manager.update_transaction(
            transaction_id, transaction_type, amount,
            category, description, date
        )

    except ValueError:
        print("Invalid ID or amount.")

def delete_transaction():
    print("\n===== DELETE TRANSACTION =====")

    try:
        transaction_id = int(input("Enter transaction ID: "))
        manager.delete_transaction(transaction_id)

    except ValueError:
        print("Please enter a valid integer ID.")

def search_transaction():
    print("\n===== SEARCH TRANSACTION =====")

    try:
        transaction_id = int(input("Enter transaction ID: "))
        manager.search_transaction(transaction_id)

    except ValueError:
        print("Please enter a valid integer ID.")

def financial_summary():
    print("\n===== FINANCIAL SUMMARY =====")

    income = report_manager.total_income()
    expense = report_manager.total_expense()
    balance = report_manager.calculate_balance()

    print("Total Income:", income)
    print("Total Expense:", expense)
    print("Current Balance:", balance)

def monthly_report():
    print("\n===== MONTHLY REPORT =====")

    month = input("Enter month (1-12): ")
    year = input("Enter year (YYYY): ")

    report_manager.monthly_report(month, year)

def category_report():
    print("\n===== CATEGORY-WISE EXPENSES =====")

    expenses = report_manager.category_wise_expense()

    if not expenses:
        print("No expenses found.")
    else:
        for category, amount in expenses.items():
            print(category, ":", amount)

def set_budget():
    print("\n===== SET MONTHLY BUDGET =====")

    try:
        month_year = input("Enter month and year (MM-YYYY): ")
        amount = float(input("Enter budget amount: "))

        budget_manager.set_budget(month_year, amount)

    except ValueError:
        print("Please enter a valid budget amount.")

def check_budget():
    print("\n===== CHECK MONTHLY BUDGET =====")

    month_year = input("Enter month and year (MM-YYYY): ")

    budget_manager.check_budget(month_year)

def view_budget():
    print("\n===== VIEW MONTHLY BUDGET =====")

    month_year = input("Enter month and year (MM-YYYY): ")

    budget_manager.view_budget(month_year)

def export_transactions():
    print("\n===== EXPORT TRANSACTIONS =====")

    csv_exporter.export_transactions(
        manager.transactions,
        "exports/transactions.csv"
    )
while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Update Transaction")
    print("4. Delete Transaction")
    print("5. Search Transaction")
    print("6. Financial Summary")
    print("7. Monthly Report")
    print("8. Category-wise Expenses")
    print("9. Set Monthly Budget")
    print("10. Check Monthly Budget")
    print("11. View Monthly Budget")
    print("12. Export Transactions to CSV")
    print("13. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_transaction()

    elif choice == "2":
        view_transactions()

    elif choice == "3":
        update_transaction()

    elif choice == "4":
        delete_transaction()

    elif choice == "5":
        search_transaction()

    elif choice == "6":
        financial_summary()

    elif choice == "7":
        monthly_report()

    elif choice == "8":
        category_report()

    elif choice == "9":
        set_budget()

    elif choice == "10":
        check_budget()

    elif choice == "11":
        view_budget()

    elif choice == "12":
        export_transactions()

    elif choice == "13":
        print("Thank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice. Please select 1-13.")

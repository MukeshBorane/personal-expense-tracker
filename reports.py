from datetime import datetime
class ReportManager:
    def __init__(self, transactions):
        self.transactions=transactions

    def total_income(self):
        total=0
        for i in self.transactions:
            if i.transaction_type=="Income":
                total+=i.amount
        return total

    def total_expense(self):
        total=0
        for i in self.transactions:
            if i.transaction_type=="Expense":
                total+=i.amount
        return total

    def calculate_balance(self):
        return self.total_income()-self.total_expense()

    def monthly_report(self, month, year):
        try:
            month = int(month)
            year = int(year)

            if month < 1 or month > 12 or year < 1:
                print("Invalid month or year.")
                return

        except ValueError:
            print("Month and year must be numbers.")
            return

        monthly_income = 0
        monthly_expense = 0
        transaction_count = 0
        
        for i in self.transactions:

            try:
                transaction_date = datetime.strptime(i.date, "%d-%m-%Y")
            except ValueError:
                print("Invalid transaction date:", i.date)
                continue

            if transaction_date.month == month and transaction_date.year == year:

                if i.transaction_type == "Income":
                    monthly_income += i.amount

                elif i.transaction_type == "Expense":
                    monthly_expense += i.amount

                transaction_count += 1

        if transaction_count == 0:
            print("No transactions found for this month.")
            return

        monthly_balance = monthly_income - monthly_expense

        print("===== MONTHLY REPORT =====")
        print("Month:", month)
        print("Year:", year)
        print("Total Income:", monthly_income)
        print("Total Expenses:", monthly_expense)
        print("Monthly Balance:", monthly_balance)

    def category_wise_expense(self):
        expense = {}

        for i in self.transactions:
            if i.transaction_type == "Expense":

                if i.category in expense:
                    expense[i.category] += i.amount

                else:
                    expense[i.category] = i.amount

        return expense
                

                

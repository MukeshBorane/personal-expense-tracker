import json
from datetime import datetime
class BudgetManager:
    def __init__(self,transactions):
        self.transactions=transactions
        self.budgets={}
        self.load_budgets()

    def set_budget(self, month_year, amount):

        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid budget amount.")
            return

        try:
            datetime.strptime(month_year, "%m-%Y")
        except ValueError:
            print("Invalid month. Use MM-YYYY format.")
            return

        old_budget = self.budgets.get(month_year)

        self.budgets[month_year] = amount

        if self.save_budgets():
            print("Budget saved successfully.")
        else:
            if old_budget is None:
                self.budgets.pop(month_year)
            else:
                self.budgets[month_year] = old_budget

            print("Could not save budget. Original budget restored.")

    def view_budget(self, month_year):
        if month_year in self.budgets:
            print("Budget of", month_year, ":", self.budgets[month_year])
        else:
            print("No budget set for this month.")

    def save_budgets(self):

        try:
            with open("data/budgets.json", "w", encoding="utf-8") as file:
                json.dump(self.budgets, file, indent=4)

            return True

        except OSError as e:
            print("Error saving budgets:", e)
            return False

    def load_budgets(self):

        try:
            with open("data/budgets.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                if not isinstance(data, dict):
                    print("Invalid budget file format.")
                    self.budgets = {}
                    return

                for month, amount in data.items():

                    try:
                        datetime.strptime(month, "%m-%Y")
                    except ValueError:
                        print("Invalid month in budget file.")
                        self.budgets = {}
                        return

                    if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
                        print("Invalid budget amount in file.")
                        self.budgets = {}
                        return

                self.budgets = data

        except FileNotFoundError:
            print("Budget file not found. Starting with empty budgets.")
            self.budgets = {}

        except json.JSONDecodeError:
            print("Budget file contains invalid JSON.")
            self.budgets = {}

        except OSError as e:
            print("Error loading budgets:", e)
            self.budgets = {}

    def calculate_monthly_expense(self, month_year):

        total = 0

        for i in self.transactions:

            try:
                transaction_date = datetime.strptime(i.date, "%d-%m-%Y")
            except ValueError:
                print("Invalid transaction date:", i.date)
                continue

            transaction_month_year = transaction_date.strftime("%m-%Y")

            if month_year == transaction_month_year and i.transaction_type == "Expense":
                total += i.amount

        return total

    def check_budget(self, month_year):

        if month_year not in self.budgets:
            print("No budget set for this month.")
            return

        monthly_budget = self.budgets[month_year]
        monthly_expense = self.calculate_monthly_expense(month_year)

        remaining_budget = monthly_budget - monthly_expense
        budget_used = (monthly_expense / monthly_budget) * 100

        print("========= Budget Report =========")
        print("Month:", month_year)
        print("Monthly Budget:", monthly_budget)
        print("Monthly Expense:", monthly_expense)
        print("Remaining Budget:", remaining_budget)
        print("Budget Used:", round(budget_used, 2), "%")

        if monthly_expense > monthly_budget:
            print("You have exceeded your monthly budget!")

        elif budget_used >= 80:
            print("Warning: You have used 80% or more of your budget!")

            
            

            



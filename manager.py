from models import Transaction
from storage import Storage
from datetime import datetime
from logger import logger

class TransactionManager:
    def __init__(self):
        self.storage = Storage()
        self.transactions = self.storage.load_transactions()

        if self.transactions:
            self.next_id = max(
                i.transaction_id for i in self.transactions
            ) + 1
        else:
            self.next_id = 1

    def add_transaction(self, transaction_type, amount,
                        category, description, date):
        if amount<=0:
            print("Invalid Amount")
            return

        if transaction_type not in ("Income", "Expense"):
            print("Invalid transaction type")
            return

        if not category.strip():
            print("Category cannot be empty.")
            return

        if not description.strip():
            print("Description cannot be empty.")
            return

        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date. Use DD-MM-YYYY.")
            return
        
        category = category.strip()
        description = description.strip()
        
        transaction=Transaction(self.next_id,transaction_type,amount,category,description,date)
        self.transactions.append(transaction)
        self.next_id+=1
        saved = self.storage.save_transactions(self.transactions)

        if saved:
            logger.info("Transaction added: ID %s", transaction.transaction_id)
            print("Transaction added successfully.")
        else:
            logger.error("Failed to add transaction: ID %s", transaction.transaction_id)
            print("Transaction could not be saved.")
            self.transactions.pop()
            self.next_id -= 1

    def view_all_transaction(self):
        if not self.transactions:
            print("No Transaction found")
        else:
            print("===================================")
            print("ALL TRANSACTIONS")
            print("===================================")
            for i in self.transactions:
                print("Transaction ID:",i.transaction_id)
                print("Transaction Type:",i.transaction_type)
                print("Amount:",i.amount)
                print("Category:",i.category)
                print("Description:",i.description)
                print("Date:",i.date,"\n")

    def search_transaction(self, transaction_id):
        
        if transaction_id <= 0:
                    print("Invalid transaction ID.")
                    return
        
        for i in self.transactions:
            if i.transaction_id == transaction_id:
                print("===================================")
                print("TRANSACTION FOUND")
                print("===================================")
                print("Transaction ID:", i.transaction_id)
                print("Transaction Type:", i.transaction_type)
                print("Amount:", i.amount)
                print("Category:", i.category)
                print("Description:", i.description)
                print("Date:", i.date)
                return

        print("Transaction not found.")

    
    def update_transaction(self, transaction_id, transaction_type,
                        amount, category, description, date):

        if transaction_id <= 0:
            print("Invalid transaction ID.")
            return

        if amount <= 0:
            print("Invalid Amount")
            return

        if transaction_type not in ("Expense", "Income"):
            print("Invalid transaction type")
            return

        if not category.strip():
            print("Category cannot be empty.")
            return

        if not description.strip():
            print("Description cannot be empty.")
            return

        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date. Use DD-MM-YYYY.")
            return

        category = category.strip()
        description = description.strip()

        for i in self.transactions:
            if i.transaction_id == transaction_id:

                old_type = i.transaction_type
                old_amount = i.amount
                old_category = i.category
                old_description = i.description
                old_date = i.date

                i.transaction_type = transaction_type
                i.amount = amount
                i.category = category
                i.description = description
                i.date = date

                saved = self.storage.save_transactions(self.transactions)

                if saved:
                    logger.info("Transaction updated: ID %s", transaction_id)
                    print("Transaction updated successfully.")
                else:
                    i.transaction_type = old_type
                    i.amount = old_amount
                    i.category = old_category
                    i.description = old_description
                    i.date = old_date

                    logger.error("Failed to update transaction: ID %s", transaction_id)
                    print("Transaction update failed. Original values restored.")

                return

        print("Transaction not found.")


    def delete_transaction(self, transaction_id):

        if transaction_id <= 0:
            print("Invalid transaction ID.")
            return

        for index, i in enumerate(self.transactions):
            if i.transaction_id == transaction_id:

                deleted_transaction = i
                self.transactions.pop(index)

                saved = self.storage.save_transactions(self.transactions)

                if saved:
                    logger.info("Transaction deleted: ID %s", transaction_id)
                    print("Transaction deleted successfully.")
                else:
                    logger.error("Failed to delete transaction: ID %s", transaction_id)
                    self.transactions.insert(index, deleted_transaction)                    
                    print("Transaction deletion failed. Original transaction restored.")

                    return

        print("Transaction not found.")

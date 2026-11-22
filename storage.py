from models import Transaction
import json
from datetime import datetime
from logger import logger

class Storage:

    def save_transactions(self, transactions):

        data = []

        for i in transactions:
            transaction_data = {
                "transaction_id": i.transaction_id,
                "transaction_type": i.transaction_type,
                "amount": i.amount,
                "category": i.category,
                "description": i.description,
                "date": i.date
            }

            data.append(transaction_data)

        try:
            with open("data/transactions.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            logger.info("Transaction saved successfully.")
            return True

        except OSError as e:
            logger.error("Error saving transactions: %s", e)
            print("Error saving transactions:", e)
            return False

    def load_transactions(self):

        transactions = []

        try:
            with open("data/transactions.json", "r") as file:
                data = json.load(file)

                if not isinstance(data, list):
                    print("Invalid transaction data format.")
                    return []

                for i in data:

                    if not isinstance(i, dict):
                        print("Invalid transaction record.")
                        return []

                    if isinstance(i["transaction_id"], bool) or not isinstance(i["transaction_id"], int) or i["transaction_id"] <= 0:
                        print("Invalid transaction ID in JSON.")
                        return []

                    if isinstance(i["amount"], bool) or not isinstance(i["amount"], (int, float)) or i["amount"] <= 0:
                        print("Invalid transaction amount in JSON.")
                        return []

                    if i["transaction_type"] not in ("Income", "Expense"):
                        print("Invalid transaction type in JSON.")
                        return []

                    if not isinstance(i["category"], str) or not i["category"].strip():
                        print("Invalid category in JSON.")
                        return []

                    if not isinstance(i["description"], str) or not i["description"].strip():
                        print("Invalid description in JSON.")
                        return []

                    if not isinstance(i["date"], str):
                        print("Invalid date in JSON.")
                        return []

                    try:
                        datetime.strptime(i["date"], "%d-%m-%Y")
                    except ValueError:
                        print("Invalid transaction date in JSON.")
                        return []
                
                    transaction = Transaction(
                        i["transaction_id"],
                        i["transaction_type"],
                        i["amount"],
                        i["category"],
                        i["description"],
                        i["date"]
                    )

                    transactions.append(transaction)

        except FileNotFoundError:
            print("Transaction file not found.")

        except json.JSONDecodeError:
            print("Error: Transaction file contains invalid JSON.")
            return []

        except KeyError as e:
            print("Transaction data is missing a required field:", e)
            return []

        except OSError as e:
            print("Error loading transactions:", e)
            return []

        return transactions
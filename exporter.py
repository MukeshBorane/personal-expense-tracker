import csv
import os

class CSVExporter:

    def export_transactions(self, transactions, filename):

        try:
            directory = os.path.dirname(filename)

            if directory:
                os.makedirs(directory, exist_ok=True)

            with open(filename, "w", newline="", encoding="utf-8") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "transaction_id",
                    "transaction_type",
                    "amount",
                    "category",
                    "description",
                    "date"
                ])

                for i in transactions:
                    writer.writerow([
                        i.transaction_id,
                        i.transaction_type,
                        i.amount,
                        i.category,
                        i.description,
                        i.date
                    ])

            print("Transactions exported successfully!")
            return True

        except OSError as e:
            print("Error exporting transactions:", e)
            return False

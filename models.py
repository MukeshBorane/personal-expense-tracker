class Transaction:
    def __init__(self,transaction_id,
        transaction_type,amount,category,
        description,date):
        self.transaction_id=transaction_id
        self.transaction_type=transaction_type
        self.amount=amount
        self.category=category
        self.description=description
        self.date=date
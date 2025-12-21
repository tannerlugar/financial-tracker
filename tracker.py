from transaction import Transaction


class TransactionManager:
    def __init__(self):
        self.transactions = []  # Empty list to start

    def add_transaction(
        self, transaction: Transaction
    ) -> None:  # Takes a Transaction object and adds it to the list
        self.transactions.append(transaction)

    def get_all_transactions(self) -> list:  # Returns the list of all transactions
        return self.transactions

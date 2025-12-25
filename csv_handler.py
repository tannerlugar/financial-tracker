import csv

from transaction import Transaction


class CSVHandler:
    def __init__(self, filename: str):
        self.filename = filename  # Store the CSV file path

    def save_transactions(
        self, transactions: list
    ) -> None:  # Save all transactions to CSV
        # Open file in write format
        with open(self.filename, "w", newline="") as f:  # 'w' = write mode (overwrites)
            writer = csv.DictWriter(
                f, fieldnames=["amount", "date", "category", "description", "type"]
            )
            # Writes the header row
            writer.writeheader()
            for transaction in transactions:
                writer.writerow(  # Writes a data row
                    {
                        "amount": transaction.amount,
                        "date": transaction.date,
                        "category": transaction.category,
                        "description": transaction.description,
                        "type": transaction.type,
                    }
                )

    def load_transactions(self) -> list: # Load all transactions from CSV
        # Create an empty list to store Treansaction objects
        transactions = []
        try:
            # Open the CSV file for reading
            with open(self.filename, "r") as f: # 'r' = read mode (does not overwrite)
                reader = csv.DictReader(f) # Create a CSV reader object
                for row in reader: # Iterate over each row in the CSV file
                    # Create a new Transaction object from that row's data
                    transaction = Transaction(float(row['amount']), row['date'], row['category'], row['description'], row['type'])
                    transactions.append(transaction) # Add the new Transaction object to the list
        except FileNotFoundError:
            # If the file does not exist, return an empty list
            pass
        return transactions # Return the list of Transaction objects



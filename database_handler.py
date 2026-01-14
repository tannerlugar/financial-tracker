import sqlite3
from transaction import Transaction

class DatabaseHandler:
    def __init__(self, filename: str):
        self.filename = filename # Store the database file path

        # Create/connect to the databse
        self.conn = sqlite3.connect(self.filename)

        # Create a cursor (this what executes SQL commands)
        cursor = self.conn.cursor()

        # Create the transactions table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                date TEXT,
                category TEXT,
                description TEXT,
                type TEXT
                )
           ''')
        
        # Save (commit) the table creation
        self.conn.commit()

    def close(self) -> None:
        '''Close the database connection'''
        if self.conn:
            self.conn.close()

    def save_transactions(self, transactions: list) -> None:
        '''Save all transactions to the databse (clears existing data first)'''
        cursor = self.conn.cursor()

        # Step 1: Delete all existing transactions
        cursor.execute("DELETE FROM transactions")

        # Step 2: Insert each transaction from the list
        for transaction in transactions:
            cursor.execute('''
                           INSERT INTO transactions (amount, date, category, description, type)
                           VALUES (?, ?, ?, ?, ?)
                           ''', (transaction.amount, transaction.date, transaction.category, transaction.description, transaction.type))
        
        # Step 3: Save (commit) all the changes
        self.conn.commit()

    def load_transactions(self,) -> list:
        '''Load all transactions from the database'''
        cursor = self.conn.cursor()

        # Query all transactions from the table
        cursor.execute("SELECT * FROM transactions")

        # Fetch all rows
        rows = cursor.fetchall()

        # Create an empty list to store Transaction objects
        transactions = []

        # Loop trhough each row and create Transactions objkects
        for row in rows:
            transaction = Transaction(
                row[1], # amount (column index 1)
                row[2], # date
                row[3], # category
                row[4], # description
                row[5], # type
                row[0]  # id 
            )
            transactions.append(transaction)

        return transactions
    
    def add_transaction(self, transaction: Transaction) -> int:
        '''Add a single transaction to the databnse and return its ID'''
        cursor = self.conn.cursor()

        cursor.execute('''
                       INSERT INTO transactions (amount, date, category, description, type)
                       VALUES (?, ?, ?, ?, ?)
                       ''', (transaction.amount, transaction.date, transaction.category,
                              transaction.description, transaction.type))
        
        self.conn.commit()

        # Return the ID that was just created
        return cursor.lastrowid
    
    def update_transaction(self, transaction: Transaction) -> None:
        '''Update an existing transaction using its ID'''
        if transaction.id is None:
            raise ValueError("Cannot update transaction without an ID")
        
        cursor = self.conn.cursor()

        cursor.execute('''
                       UPDATE transactions
                       SET amount = ?, date = ?, category = ?, description = ?, type = ?
                       WHERE id = ?
                       ''', (transaction.amount, transaction.date, transaction.category,
                             transaction.description, transaction.type, transaction.id))
        
        self.conn.commit()

    def delete_transaction(self, transaction_id: int) -> None:
        '''Delete a single transaction by its ID'''
        cursor = self.conn.cursor()

        cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id))

        self.conn.commit()
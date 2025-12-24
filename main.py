from csv_handler import CSVHandler
from tracker import TransactionManager
from transaction import Transaction

# Create manager and handler
manager = TransactionManager()
csv_handler = CSVHandler('data/transactions.csv')

# Add some transactions
manager.add_transaction(Transaction(-40.00, '12/14/2025', 'Car', 'Gas', 'expense'))
manager.add_transaction(Transaction(1000.00, '12/01/2025', 'Salary', 'Paycheck', 'income'))

# Save to CSV
csv_handler.save_transactions(manager.get_all_transactions())
print('Saved!')

#Load from CSV
loaded = csv_handler.load_transactions()
print('\nLoaded transactions:')
for t in loaded:
    print(t)

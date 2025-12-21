from tracker import TransactionManager
from transaction import Transaction

manager = TransactionManager()

manager.add_transaction(Transaction(-40.00, "12/14/2025", "Car", "Gas", "expense"))
manager.add_transaction(
    Transaction(1000.00, "12/01/2025", "Salary", "Paycheck", "income")
)

for t in manager.get_all_transactions():
    print(t)

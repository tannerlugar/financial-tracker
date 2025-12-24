from tracker import TransactionManager 
from csv_handler import CSVHandler
from transaction import Transaction

class CLI:
    def __init__(self, manager: TransactionManager, csv_handler: CSVHandler):
        self.manager = manager # Reference to the Transaction Manager
        self.csv_handler = csv_handler # Reference to the CSV Handler
    
    def display_menu(self) -> None:
        print("=== Financial Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. View Summary")
        print("5. Exit")
        print()
        print("Enter choice: ", end='')
    
    def run(self) -> None:
        # Load Transactions at startup
        self.manager.transactions = self.csv_handler.load_transactions()

        while True:
            self.display_menu()

            choice = input()

            if choice == '1':
                self.add_income()     
            elif choice == '2':
                self.add_expense()
            elif choice == '3':
                self.view_all_transactions()           
            elif choice == '4':
                self.view_summary()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, Please try again.")

    def add_income(self) -> None:
        # Prompt user for income details
        amount = float(input("Enter income amount: "))
        date = input("Enter date (MM/DD/YYYY): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        #Create a Transaction object
        income = Transaction(amount, date, category, description, "income")
        # Add to Transaction Manager
        self.manager.add_transaction(income)
        # Save to CSV
        self.csv_handler.save_transactions(self.manager.get_all_transactions())
        print("Income added successfully.")

    def add_expense(self) -> None:
        # Prompt user for expense details
        amount = float(input("Enter expense amount: "))
        date = input("Enter date (MM/DD/YYYY): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        # Create a Transaction object
        expense = Transaction(-amount, date, category, description, "expense")
        #A Add to Transaction Manager
        self.manager.add_transaction(expense)
        # Save to CSV
        self.csv_handler.save_transactions(self.manager.get_all_transactions())
        print("Expense added successfully.")

    def view_all_transactions(self) -> None:
        # Get all transactions from the Transaction Manager
        transactions = self.manager.get_all_transactions()
        # If list is empty, print message
        if not transactions:
            print("No transactions available.")
        else:
            # Display all transactions
            for transaction in transactions:
                print(transaction)
    
    def view_summary(self) -> None:
        # Get all transactions from the Transaction Manager
        transaction = self.manager.get_all_transactions()
        # If list is empty, print message
        if not transaction:
            print("No transactions available.")
        else:
            # Calculate total income and expenses
            total_income = sum(t.amount for t in transaction if t.type == "income")
            total_expenses = sum(t.amount for t in transaction if t.type == "expense")
            # Calculate balance
            balance = total_income + total_expenses
            # Print Summary
            print("=== Summary ===")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expenses: ${abs(total_expenses):.2f}")
            print(f"Balance: ${balance:.2f}")
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
        print("6. Delete Transaction")
        print("7. Update Transaction")
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
            elif choice == '6':
                self.delete_transaction()
            elif choice == '7':
                self.edit_transaction()
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
    
    def delete_transaction(self) -> None:
        # Get all transactions from the Transaction Manager
        transactions = self.manager.get_all_transactions()
        # If empty, show message and return
        if not transactions:
            print("No transactions available to delete.")
            return
        # Display transactions with indices
        for idx, transaction in enumerate(transactions):
            print(f"{idx + 1}. {transaction}")
        # Get user input (number or 'c')
        choice = input("Enter the number of the transaction to delete (or 'c' to cancel): ")
        # If 'c', return (cancel)
        if choice.lower() == 'c':
            print("Deletion cancelled.")
            return
        # Validate the number (is it a valid index?)
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(transactions):
                print("Invalid selection. Please try again.")
                return
        except ValueError:
            print("Invalid input. Please enter a number or 'c' to cancel.")
            return
        # Show the transaction and confirm (y/n)   
        transaction_to_delete = transactions[index]
        confirm = input(f"Are you sure you want to delete the following transaction? (y/n)\n{transaction_to_delete}\n")
        if confirm.lower() != 'y':
            print("Deletion cancelled.")
            return
        # If yes, delete from manager's list
        self.manager.delete_transaction(index)
        # Save to CSV
        self.csv_handler.save_transactions(self.manager.get_all_transactions())
        print("Transaction deleted successfully.")

    def edit_transaction(self) -> None:
        # Get all transactions from the Transaction Manager
        transactions = self.manager.get_all_transactions()
        # If empty, show message and return
        if not transactions:
            print("No transactions available to update.")
            return
        # Display transactions with indices
        for idx, transaction in enumerate(transactions):
            print(f"{idx + 1}. {transaction}")
        # Get user input (number or 'c')
        choice = input("Enter the number of the transaction to update (or 'c' to cancel): ")
        # if 'c', return (cancel)
        if choice.lower() == 'c':
            print("Update cancelled.")
            return
        # Validate the number (is it a valid index?)
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(transactions):
                print("Invalid selection. Please try again.")
                return
        except ValueError:
            print("Invalid input. Please enter a number or 'c' to cancel.")
            return
        # Get the transaction to edit
        transaction_to_edit = transactions[index]
        print(f"Editing transaction: {transaction_to_edit}")
        # For each field (amount, date, category, description): - Show current value - Get new value (or press Enter to keep current)
        new_amount = input(f"Enter new amount (current: {transaction_to_edit.amount}) or press Enter to keep: ")
        new_date = input(f"Enter new date (current: {transaction_to_edit.date}) or press Enter to keep: ")
        new_category = input(f"Enter new category (current: {transaction_to_edit.category}) or press Enter to keep: ")
        new_description = input(f"Enter new description (current: {transaction_to_edit.description}) or press Enter to keep: ")
        # Handle amount - auto-negate for expenses, keep positive for income
        if new_amount:
            amount = float(new_amount)
            # Ensure correct sign based on type
            if transaction_to_edit.type == 'expense' and amount > 0:
                amount = -abs(amount) # Always negative
            else: # income
                amount = abs(amount) # Always positive
        else:
            amount = transaction_to_edit.amount
        # Create NEW Transaction with updated values (keep same type!)
        updated_transaction = Transaction(
            amount, # Use the processed amount
            new_date if new_date else transaction_to_edit.date,
            new_category if new_category else transaction_to_edit.category,
            new_description if new_description else transaction_to_edit.description,
            transaction_to_edit.type
        )
        # Replace old transaction in list
        self.manager.transactions[index] = updated_transaction
        # Save to CSV
        self.csv_handler.save_transactions(self.manager.get_all_transactions())
        print("Transaction updated successfully")

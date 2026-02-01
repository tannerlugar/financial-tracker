from tracker import TransactionManager 
from database_handler import DatabaseHandler
from transaction import Transaction
from datetime import datetime

INCOME_CATEGORIES = [
    "Salary",
    "Freelance/Side Hustle",
    "Other Income"
]

EXPENSE_CATEGORIES = [
    "Food & Groceries",
    "Transportation",
    "Bills & Utilities",
    "Entertainment",
    "Shopping",
    "Healthcare"
]

class CLI:
    def __init__(self, manager: TransactionManager, db_handler: DatabaseHandler):
        self.manager = manager # Reference to the Transaction Manager
        self.db_handler = db_handler # Reference to Storage Manager
    
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
        self.manager.transactions = self.db_handler.load_transactions()

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
        category = self.select_category('income') 
        description = input("Enter description: ")
        #Create a Transaction object (no ID)
        income = Transaction(amount, date, category, description, "income")
        # Save to database and get the new ID
        new_id = self.db_handler.add_transaction(income)
        # Set the ID on transaction object
        income.id = new_id
        # Save to CSV
        self.manager.add_transaction(income)
        print("Income added successfully.")

    def add_expense(self) -> None:
        # Prompt user for expense details
        amount = float(input("Enter expense amount: "))
        date = input("Enter date (MM/DD/YYYY): ")
        category = self.select_category('expense')
        description = input("Enter description: ")
        # Create a Transaction object
        expense = Transaction(-amount, date, category, description, "expense")
        # Save to database and get the new ID
        new_id = self.db_handler.add_transaction(expense)
        # Set the ID on transaction object
        expense.id = new_id
        # Save to CSV
        self.manager.add_transaction(expense)
        print("Expense added successfully.")

    def view_all_transactions(self) -> None:
        # Get all transactions from the Transaction Manager
        transactions = self.manager.get_all_transactions()
        # If list is empty, print message
        if not transactions:
            print("No transactions available.")
            return
        # Show filter options
        print("\nView Options:")
        print("1. All Transactions")
        print("2. Filter by Date Range")
        print("3. This Month Only")
        choice = input("Enter choice: ")

        if choice == '1':
            # Show all (current behavior)
            print("\n=== All Transactions ===")
            for transaction in transactions:
                print(transaction)
        elif choice == '2':
            # Filter by Date Range
            start_date_str = input("Enter start date (MM/DD/YYYY): ")
            end_date_str = input("Enter end date (MM/DD/YYYY): ")

            # Convert strings to datetime objects
            start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
            end_date = datetime.strptime(end_date_str, "%m/%d/%Y")

            print(f"\n=== Transactions from {start_date_str} to {end_date_str} ===")
            for transaction in transactions:
                trans_date = datetime.strptime(transaction.date, "%m/%d/%Y")
                if start_date <= trans_date <= end_date:
                    print(transaction)
        elif choice == '3':
            # This Month Only
            current_month = datetime.now().month
            current_year = datetime.now().year
            print(f"\n=== Transactions for {current_month}/{current_year} ===")
            for transaction in transactions:
                trans_date = datetime.strptime(transaction.date, "%m/%d/%Y")
                if trans_date.month == current_month and trans_date.year == current_year:
                    print(transaction)
                else:
                    continue
        else:
            print("Invalid choice.")
            return
        
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
        # Delete from database using transaction ID
        self.db_handler.delete_transaction(transaction_to_delete.id)
        # Delete from manager's in-memory list
        self.manager.delete_transaction(index)
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
        print(f'\nCurrent category: {transaction_to_edit.category}')
        change_category = input("Change category? (y/n): ")
        if change_category.lower() == 'y':
            new_category = self.select_category(transaction_to_edit.type)
        else:
            new_category = transaction_to_edit.category
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
            transaction_to_edit.type,
            transaction_to_edit.id
        )
        # Update in database using ID
        self.db_handler.update_transaction(updated_transaction)
        # Replace in manager's list
        self.manager.transactions[index] = updated_transaction
        print("Transaction updated successfully")
    
    def select_category(self, transaction_type: str) -> str:
        # Choose the right category list based on type
        if transaction_type == 'income':
            categories = INCOME_CATEGORIES
        else:
            categories = EXPENSE_CATEGORIES

        # Display categories
        print("\nSelect category:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        print(f"{len(categories) + 1}. Custom (Enter your own)")

        # Get user choice
        choice = input("Enter choice: ")

        # Validate choice and return category
        try:
            index = int(choice) - 1
            if 0 <= index < len(categories):
                return categories[index]
            elif index == len(categories):
                custom_category = input("Enter custom category: ")
                return custom_category
            else:
                print("Invalid choice. Using 'Other'.")
                return 'Other'
        except ValueError:
            print("Invalid input. Using 'Other'.")
            return 'Other'

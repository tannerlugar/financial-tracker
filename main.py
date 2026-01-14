from tracker import TransactionManager
from database_handler import DatabaseHandler 
from cli import CLI

def main():
    # Create the core objects
    manager = TransactionManager()
    db_handler = DatabaseHandler('data/transactions.db')
    
    try:
        # Create and run CLI
        cli = CLI(manager, db_handler)
        cli.run()
    finally:
        # Always close the database, even if there's an error
        db_handler.close()

if __name__ == "__main__":
    main()
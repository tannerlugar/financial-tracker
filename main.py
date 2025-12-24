from tracker import TransactionManager
from csv_handler import CSVHandler
from cli import CLI

def main():
    # Create the core objects
    manager = TransactionManager()
    csv_handler = CSVHandler('data/transactions.csv')
    
    # Create and run CLI
    cli = CLI(manager, csv_handler)
    cli.run()

if __name__ == "__main__":
    main()
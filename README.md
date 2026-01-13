# Financial Tracker

A command-line personal finance tracker built with Python. Track your income and expenses with persistent CSV storage and view detailed summaries of your financial activity.

## 🚧 Current Status

**Actively in development** - Core CLI features complete, currently migrating from CSV to SQLite database for improved performance and scalability.

## Features

- ✅ **Add Income & Expenses** - Record transactions with amount, date, category, and description
- ✅ **View All Transactions** - Display complete transaction history with filtering options (date range, current month)
- ✅ **Edit & Delete Transactions** - Modify or remove existing records
- ✅ **Financial Summary** - See total income, total expenses, and current balance
- ✅ **CSV Persistence** - All data automatically saved to CSV for future sessions
- ✅ **Clean CLI Interface** - Simple, intuitive menu-driven interaction

## Installation

1. Clone the repository:
```
git clone https://github.com/tannerlugar/financial-tracker.git
cd financial-tracker
```
2. Run the program (Python 3.x required):
python3 main.py

No external dependencies required - uses only Python standard library!

## Usage

The program presents a simple menu:
=== Financial Tracker ===
1. Add Income
2. Add Expense
3. View All Transactions
4. View Summary
5. Exit
6. Delete Transaction
7. Update Transaction

**Example workflow:**
- Select `1` to add income (salary, freelance payment, etc.)
- Select `2` to add an expense (groceries, gas, bills, etc.)
- Select `3` to view all your transactions (with filtering options)
- Select `4` to see your financial summary
- Select `5` to exit (data is auto-saved!)

## Project Structure

financial-tracker/
├── main.py              # Entry point
├── transaction.py       # Transaction class definition
├── tracker.py          # TransactionManager (business logic)
├── csv_handler.py      # CSV read/write operations
├── database_handler.py # SQLite persistence (in progress)
├── cli.py              # Command-line interface
└── data/
    └── transactions.csv # Your transaction data (auto-generated)

## Technical Highlights

- **Separation of Concerns** - Data model, business logic, storage, and UI are cleanly separated into distinct classes
- **OOP Design** - Uses classes (Transaction, TransactionManager, CSVHandler) with single responsibility principle
- **Swappable Storage Backend** - Handler pattern allows easy migration from CSV to SQLite without changing business logic
- **Input Validation** - Handles edge cases like invalid dates, negative amounts, and empty fields

## Technologies Used

- **Python 3** - Core language
- **CSV module** - Data persistence
- **SQLite3** - Database migration (in progress)
- **OOP principles** - Clean, modular architecture

## What I Learned

This was my first multi-file Python project, built to practice:
- Object-oriented programming (classes, methods, encapsulation)
- File I/O and CSV manipulation
- Building user-friendly CLI applications
- Project organization and structure
- Version control with Git/GitHub

## Future Enhancements

- [ ] Complete SQLite database migration
- [ ] Budget tracking and alerts
- [ ] Category-based spending reports
- [ ] Data visualization (charts/graphs)
- [ ] Flask web interface
- [ ] Export to Excel/PDF

## Why This Project?

Built to demonstrate practical Python skills for automation and data management work. This project showcases my ability to build real applications from scratch, think through user experience, and write maintainable code skills directly applicable to Python automation development.

## License

MIT License - see [LICENSE](LICENSE) file for details

## Author

Built as a learning project by [Tanner Lugar](https://github.com/tannerlugar)
- Aspiring Python automation developer

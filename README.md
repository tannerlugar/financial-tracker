# Financial Tracker

A command-line personal finance tracker built with Python. Track your income and expenses with persistent CSV storage and view detailed summaries of your financial activity.

## Features

- ✅ **Add Income & Expenses** - Record transactions with amount, date, category, and description
- ✅ **View All Transactions** - Display complete transaction history
- ✅ **Financial Summary** - See total income, total expenses, and current balance
- ✅ **CSV Persistence** - All data automatically saved to CSV for future sessions
- ✅ **Clean CLI Interface** - Simple, intuitive menu-driven interaction

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tannerlugar/financial-tracker.git
cd financial-tracker
```

2. Run the program (Python 3.x required):
```bash
python3 main.py
```

No external dependencies required - uses only Python standard library!

## Usage

The program presents a simple menu:
```
=== Financial Tracker ===
1. Add Income
2. Add Expense
3. View All Transactions
4. View Summary
5. Exit
```

**Example workflow:**
- Select `1` to add income (salary, freelance payment, etc.)
- Select `2` to add an expense (groceries, gas, bills, etc.)
- Select `3` to view all your transactions
- Select `4` to see your financial summary
- Select `5` to exit (data is auto-saved!)

## Project Structure
```
financial-tracker/
├── main.py              # Entry point
├── transaction.py       # Transaction class definition
├── tracker.py          # TransactionManager (business logic)
├── csv_handler.py      # CSV read/write operations
├── cli.py              # Command-line interface
└── data/
    └── transactions.csv # Your transaction data (auto-generated)
```

## Technologies Used

- **Python 3** - Core language
- **CSV module** - Data persistence
- **OOP principles** - Clean, modular architecture

## What I Learned

This was my first multi-file Python project, built to practice:
- Object-oriented programming (classes, methods, encapsulation)
- File I/O and CSV manipulation
- Building user-friendly CLI applications
- Project organization and structure
- Version control with Git/GitHub

## Future Enhancements

- [ ] Budget tracking and alerts
- [ ] Category-based spending reports
- [ ] Data visualization (charts/graphs)
- [ ] Edit/delete existing transactions
- [ ] Export to Excel/PDF
- [ ] Date range filtering

## License

MIT License - see [LICENSE](LICENSE) file for details

## Author

Built as a learning project by [Tanner Lugar](https://github.com/tannerlugar)
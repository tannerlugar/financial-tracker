class Transaction:
    def __init__(self, amount, date, category, description, type, id=None):
        self.id = id # Will be None for new transactions, assigned by DB when loaded
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.type = type

    def __str__(self) -> str:  # __str__ to display it nicely
        return "{} | {} | ${:.2f} | {} | {}".format(
            self.date, self.category, self.amount, self.description, self.type
        )

    def is_expense(self) -> bool:
        return self.type == 'expense'
    
    def is_income(self) -> bool:
        return self.type == 'income'

    def get_absolute_amount(self) -> float:
        # Return the amount as a positive number (remove negative sign)
        return abs(self.amount)

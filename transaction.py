class Transaction:
    def __init__(self, amount, date, category, description, type):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.type = type

    def __str__(self) -> str:  # __str__ to display it nicely
        return "{} | {} | ${:.2f} | {} | {}".format(
            self.date, self.category, self.amount, self.description, self.type
        )

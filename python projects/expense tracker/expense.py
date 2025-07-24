from datetime import datetime

class Expense:
    def __init__(self, title, amount, category, date=None):
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

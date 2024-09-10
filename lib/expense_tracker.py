class ExpenseTracker:
    def __init__(self, name):
        self.name = name
        self.expenses = []
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]
    
class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []
        self.expenses = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= self.balance

    def add_expense(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.expenses += amount
            self.balance -= amount
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


class MonthlyBudget:
    def __init__(self, year, month, budget_amount):
        self.year = year
        self.month = month
        self.categories = {}
        self.budget_amount = budget_amount

    def add_category(self, category):
        self.categories[category.name] = category

    def add_expense_to_category(self, category_name, expense_amount, expense_description):
        if category_name in self.categories:
            category = self.categories[category_name]
            if category.check_funds(expense_amount):
                category.withdraw(expense_amount, expense_description)
                return True
        return False

    def get_total_expenses(self):
        total_expenses = 0
        for category in self.categories.values():
            total_expenses += category.get_balance()
        return total_expenses

    def get_balance(self):
        balance = self.budget_amount - self.get_total_expenses()
        return balance
    
class Budget:
    def __init__(self):
        self.categories = {}
        self.budget = 0

    def add_category(self, category_name):
        if category_name in self.categories:
            print(f"Category '{category_name}' already exists.")
        else:
            self.categories[category_name] = Category(category_name)

    def deposit(self, category_name, amount):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist.")
        else:
            self.categories[category_name].deposit(amount)

    def withdraw(self, category_name, amount):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist.")
        elif self.categories[category_name].balance < amount:
            print(f"Insufficient funds in category '{category_name}'.")
        else:
            self.categories[category_name].withdraw(amount)

    def get_balance(self, category_name):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist.")
        else:
            return self.categories[category_name].balance

    def set_budget(self, amount):
        self.budget = amount

    def get_budget(self):
        return self.budget

    def get_category_names(self):
        return list(self.categories.keys())
    
    
def main():
    # Create some budget categories
    categories = {
        "groceries": Category("Groceries"),
        "clothing": Category("Clothing"),
        "housing": Category("Housing"),
        "entertainment": Category("Entertainment"),
        "transportation": Category("Transportation"),
    }

    # Create a new budget instance
    my_budget = Budget(categories)

    # Deposit some money into each category
    my_budget.deposit_funds("groceries", 500)
    my_budget.deposit_funds("clothing", 100)
    my_budget.deposit_funds("housing", 1000)
    my_budget.deposit_funds("entertainment", 50)
    my_budget.deposit_funds("transportation", 200)

    # Set a budget for the month
    monthly_budget = 1500

    # Display the budget status
    print("Current Budget Status:")
    print("=======================")
    for category in my_budget.categories:
        print(my_budget.categories[category].name + ":", my_budget.get_balance(category))
    print("Total Balance:", my_budget.get_total_balance())
    print("Monthly Budget:", monthly_budget)
    print("Budget Remaining:", monthly_budget - my_budget.get_total_balance())

if __name__ == "__main__":
    main()
    
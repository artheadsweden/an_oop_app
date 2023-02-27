from budget1 import Category, MonthlyBudget

def test_add_expense():
    category = Category('Food')
    category.deposit(1000)
    category.add_expense(250)
    assert category.get_balance() == 750

def test_create_monthly_budget():
    monthly_budget = MonthlyBudget(2022, 'January', 1000)
    assert monthly_budget.get_balance() == 1000

def test_add_category_to_monthly_budget():
    monthly_budget = MonthlyBudget(2022, 'January', 1000)
    category = Category('Food')
    monthly_budget.add_category(category)
    assert len(monthly_budget.categories) == 1

def test_add_expense_to_monthly_budget_category():
    monthly_budget = MonthlyBudget(2022, 'January', 1000)
    category = Category('Food')
    category.deposit(1000, 'Food Expenses')
    monthly_budget.add_category(category)
    monthly_budget.add_expense_to_category('Food', 250, 'Pizza')
    assert category.get_balance() == 750

def test_total_expenses():
    monthly_budget = MonthlyBudget(2022, 'January', 1000)
    category1 = Category('Food')
    category1.deposit(1000)
    category2 = Category('Entertainment')
    category2.deposit(500)
    monthly_budget.add_category(category1)
    monthly_budget.add_category(category2)
    monthly_budget.add_expense_to_category('Food', 250, 'Pizza')

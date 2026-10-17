import datetime
from Commands.load_save import read_expense, write_expense, find_max_expense

def add_expense(amount, category, description):
    loading_expenses = read_expense()
    next_id = find_max_expense(loading_expenses) + 1 
    expense = {
        'ID' : next_id,
        "Amount" : float(amount),
        "Category" : category.title(),
        "Description" : description.title(),
        "Date" : str(datetime.date.today())
    }
    loading_expenses.append(expense)

    write_expense(loading_expenses)
    



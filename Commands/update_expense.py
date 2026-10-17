from Commands.load_save import read_expense, write_expense, find_expense

def update_key(id, key, value):
        expenses= read_expense()
        target = find_expense(id, expenses)
        expenses[expenses.index(target)][key] = value
        write_expense(expenses)



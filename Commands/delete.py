from Commands.load_save import find_expense, read_expense, write_expense

def delete_expense(id):
    expenses = read_expense()
    target = find_expense(id, expenses)
    if target:
        expenses.remove(target)
        write_expense(expenses)
        return True
    else:
        print(f'Expense with ID {id} was not found.'.title())
        return False
        



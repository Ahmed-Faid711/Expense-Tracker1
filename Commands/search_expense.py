from Commands.load_save import read_expense
def search(value, key):
    target = []
    expenses = read_expense()
    for expense in expenses:
        if value.lower().strip() in expense[key].lower().strip():
            target.append(expense)
        
    return target
    

def search_amount(value):
    target = []
    expenses = read_expense()
    for expense in expenses:
        if value == expense["Amount"]:
            target.append(expense)
        
    return target


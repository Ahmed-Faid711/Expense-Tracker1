from Commands.load_save import read_expense, find_expense
def is_valid_amount(amount):
    try:
        if float(amount) > 0 :
            return True
        else:
            return False
    except ValueError :
            return False

def is_valid(id):
    try:
        check = int(id)
        if check > 0:
            if str(check) == str(id):
                return True
            else:
                 return False
        else:
             return False
    except ValueError:
            return False

def is_exist(id):
    expenses = read_expense()
    return find_expense(int(id), expenses)


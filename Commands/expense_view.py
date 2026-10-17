from Commands.load_save import read_expense ,find_expense
from Commands.data_validation import is_valid


def show(expenses):
    if expenses:
        print("ID       Amount      Category                Description             Date")
        print("-"*80)
        for expense in expenses:
            print(f"{expense['ID']:<8} {expense['Amount']:<11} {expense['Category']:<23} {expense['Description']:<23} {expense['Date']}")
    else:
         print('Not Found')
      

def show_list():
    expenses = read_expense()
    if not expenses:
        print('there is no expenses'.capitalize())
    else:
        print("ID       Amount      Category                Description             Date")
        print("-"*80)

        for expense in expenses:
                print(f"{expense['ID']:<8} {expense['Amount']:<11} {expense['Category']:<23} {expense['Description']:<23} {expense['Date']}")



def show_expense(id):
    expenses = read_expense()
    target = find_expense(id,expenses)
    if not expenses:
            print('there is no expenses'.title())
    elif not is_valid(id) or not target :
        print("Invalid ID")
    
    else:
        show([target])


    

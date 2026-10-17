import json 

def read_expense():
    try:
        with open('/home/ahmed-f/Projects/Expense-Tracker/expenses.json','r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_expense(expenses):
    with open('/home/ahmed-f/Projects/Expense-Tracker/expenses.json','w') as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)
    
def find_expense(id, data):
    expenses = data
    for expense in expenses:
        if expense["ID"] == id:
            return expense 
            
    else:
        return None

def find_max_expense(data):
    expenses = data
    max_id = 0
    for expense in expenses:
        max_id = max(max_id,expense["ID"])
    return max_id
    





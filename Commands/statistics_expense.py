from Commands.load_save import read_expense
from Commands.search_expense import search_amount, search
import datetime

def get_data(key,expenses = None):
    if expenses == None:
        expenses = read_expense()
    data = []
    for expense in expenses:
        data.append(expense[key])
    return data

def total_expenses():
    return sum(get_data("Amount"))

def average_expense():
    try:
        return total_expenses()/ len(get_data("Amount"))
    except ZeroDivisionError:
        print("there is no expenses".title())
        return 0

def highest_expense():
    max_amount = max(get_data("Amount"))
    return search_amount(max_amount)

def lowest_expense():
    min_amount = min(get_data("Amount"))
    return search_amount(min_amount)

def expense_category():
    ordered = {}
    expenses = {}
    categories = set(get_data("Category"))
    
    for category in categories:
       expenses[category] = search(category,"Category")
       
    for expense in expenses:
        ordered[expense] = get_data("Amount" , expenses[expense])
    for key, value in ordered.items():
        ordered[key] = sum(value)
    return ordered 

def montly_summary(month):
    current_year = str(datetime.datetime.now().year)
    date = current_year+'-'+month.zfill(2)+'-'
    return search(date ,'Date')



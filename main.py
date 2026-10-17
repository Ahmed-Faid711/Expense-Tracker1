from Commands import add 
from Commands import expense_view
from Commands import delete
from Commands.update_expense import update_key
from Commands.data_validation import is_valid, is_valid_amount, is_exist
from Commands.search_expense import search ,search_amount
from Commands import statistics_expense


while True:
    ##########HeadLine##########

    print('='*30)
    print("Expense Tracker".center(30))
    print('='*30)
    print('1- Add Expense')
    print('2- View Expenses')
    print('3- Delete Expense')
    print('4- Update Expense')
    print('5- Search Expenses')
    print('6- Statistics')
    print('7- Exit')
    print('='*30)

    ############################

    #########ChoiceLogic########

    choise = input(("What do you want to do: ".title())).strip()


    match choise:
        case '1':
            amount = input("Enter The Amount: ")
            if not is_valid_amount(amount):
                print("Invalid Amount")
                
            else:
                category = input("Enter The Category: ")
                description = input("Enter The Description: ")
                add.add_expense(amount,category,description)

        case '2':
            print('1- View List')
            print('2- View Expense')
            choise = input().strip()
            match choise :
                case "1":
                    expense_view.show_list()
                case "2":
                    id = input("What Is Expense ID: ").strip()
                    if not is_valid(id):
                        print("Invalid ID")
                    else:
                        expense_view.show_expense(int(id))
                    

        case '3':
            
            id = input("which expense do you want to delete: ".title()).strip()
            if not is_valid(id):
                print("Invalid ID")

            else:
                id = int(id)
                is_deleted = delete.delete_expense(id)
                if is_deleted:
                    print(f'Expense {id} deleted successfully.')
                
        case '4':
            id = input("which expense do you want to update: ".title()).strip()
            if is_valid(id) and is_exist(id):
                id = int(id)
        
                ##########UpdateHeadLine##########
                print('='*30)
                print("Update".center(30))
                print('='*30)
                print('1- Amount')
                print('2- Category')
                print('3- Description')
                print('='*30)
                ##################################

                key = input("what do you want to update: ".title()).strip()

                match key:
                    case '1':    
                        value = input("updated value is: ".title()).strip()
                        if is_valid_amount(value):
                            update_key(id, 'Amount', float(value))
                            print('expense updated'.title())
                        else:
                            print('Invalid Amount')
                    case '2':    
                        value = input("updated value is: ".title()).strip()
                        update_key(id, 'Category', value)
                        print('expense updated'.title())
                    case '3':    
                        value = input("updated value is: ".title()).strip()
                        update_key(id, 'Description', value)
                        print('expense updated'.title())
            
            else:
                print("Invalid ID")
        case '5':


            ##########SearchHeadLine##########
            print('='*30)
            print("Search".center(30))
            print('='*30)
            print('1- Amount')
            print('2- Category')
            print('3- Description')
            print('4- date')
            print('='*30)
            ###################################


            key = input('Search By: ').strip()
            match key:
                case '1':
                    value = input('enter the amount: '.title())
                    if is_valid_amount(value):
                        expense_view.show(search_amount(float(value)))
                    else:
                        print('Invalid Amount')
                case '2':
                    value = input('enter the Category: '.title())
                    expense_view.show(search(value, "Category"))
                case '3':
                    value = input('enter the Description: '.title())
                    expense_view.show(search(value, "Description"))
                case '4':
                    value = input('enter the date: '.title())
                    expense_view.show(search(value, "Date"))


        case '6':


            #######StatisticscsHeadLine#######
            print('='*30)
            print("Statistics".center(30))
            print('='*30)
            print('1- Total expenses')
            print('2- Average expense')
            print('3- Highest expense')
            print('4- Lowest expense')
            print('5- Expenses By Category')
            print('6- break')
            print('='*30)
            ###################################

            choise = input('What Do You Want To Do: ').strip()
            match choise:
                case '1':
                    print(f'Total Expenses: {statistics_expense.total_expenses()}')
                case '2':
                    print(f'Average Expense: {statistics_expense.average_expense()}')
                case '3':
                    print('Highest Expense:')
                    expense_view.show(statistics_expense.highest_expense())
                case '4':
                    print('Lowest Expense:')
                    expense_view.show(statistics_expense.lowest_expense())
                case '5':
                    print('='*30)
                    print("Expenses By Category".center(30))
                    print('='*30)
                    expenses = statistics_expense.expense_category()
                    for key, value in expenses.items():
                        print(f'{key}: {value}')

                case '6':
                    pass
        case '7':
            break
    ##########################################
            
                
            

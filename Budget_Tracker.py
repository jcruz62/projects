# Budget Tracker
# 1. Set a Budget
# 2. Add expenses, description
# 3. Output leftover budget
# need a way to store saved data
# reset budget
# edit items

# imports used
import json


def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f'Added expenses: {description}, Amount: {amount}')

def show_budget_details(budget, expenses):
    print(f"Total Budget: {budget}")
    print("Expenses")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget:{get_balance(budget, expenses)}")
    

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_budget'], data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget, 
        'expenses': expenses, 
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)



def main():
    print("Welcome to the Budget Tracker App!")
    # a place to store data
    filepath = 'budget_data.json'
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        initial_budge1 = float(input("Enter your initial budget: "))
    budget = initial_budget
    
    # create options
    while True:
        print("What would you like to do?")
        print("1. Add an expense: ")
        print("2. Show budget details: ")
        print("3. Remove an item: ")
        print('4. Reset Budget')
        print("5. Exit")
        choice = input("Enter your choice(1/2/3/4/5): ")
    
        # use if-else for action for each option
        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense item price: "))
            add_expense(expenses, description, amount)
        elif choice == '2':
            show_budget_details(budget, expenses)
        elif choice == '3':
            remove = input("Enter item to remove: ")
            removed = False
            for expense in expenses: 
                if expense['description'] == remove:
                    expenses.remove(expense)
                    removed =True
                    print(f"Expense '{remove} removed success")
                    break
                if not removed:
                    print(f"No item found with the name '{remove}")
                    
        elif choice == '4':
            new_initial_budget = float(input("Enter new initial Budget: "))
            initial_budget = new_initial_budget
            save_budget_details(filepath, initial_budget, expenses)
            print("Successfully reset initial budget!")
        elif choice == '5':
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting Budget Tracker App")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
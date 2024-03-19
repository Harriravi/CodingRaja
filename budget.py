import json
import os

# Function to load data from file
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}

# Function to save data to file
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

# Function to add income
def add_income(data):
    income = float(input("Enter income amount: "))
    data['income'] += income
    print(f"Income of ${income} added successfully.")
    save_data(data, FILE_NAME)

# Function to add expense
def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    print(f"Expense of ${amount} in {category} category added successfully.")
    save_data(data, FILE_NAME)

# Function to calculate remaining budget
def calculate_budget(data):
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    print(f"Remaining Budget: ${remaining_budget}")

# Function to analyze expenses by category
def analyze_expenses(data):
    expense_categories = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    print("Expense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount}")

# Main function
def main():
    global FILE_NAME
    FILE_NAME = "budget_data.json"
    budget_data = load_data(FILE_NAME)

    while True:
        print("\n===== Budget Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_income(budget_data)
        elif choice == '2':
            add_expense(budget_data)
        elif choice == '3':
            calculate_budget(budget_data)
        elif choice == '4':
            analyze_expenses(budget_data)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

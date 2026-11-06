# Budget Calculator Algorithm
# Created by Maurine Kyalo

def calculate_budget():
    print("Welcome to the Monthly Budget Calculator!")
    
    # 1. Input Income
    income = float(input("Enter your monthly income: "))
    
    # 2. Input Fixed Expenses
    fixed_expenses = float(input("Enter your fixed expenses (rent, utilities): "))
    
    # 3. Variable Expenses Loop
    variable_expenses = 0.0
    while True:
        add_expense = input("Do you have a variable expense to add? (yes/no): ").lower()
        if add_expense == 'yes':
            expense = float(input("Enter the expense amount: "))
            variable_expenses += expense
        elif add_expense == 'no':
            break
        else:
            print("Please type 'yes' or 'no'.")
            
    # 4. Calculate Remaining Budget
    total_expenses = fixed_expenses + variable_expenses
    remaining_budget = income - total_expenses
    
    # 5. Display Results with Conditional Selection
    print("\n--- Budget Summary ---")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Remaining Budget: {remaining_budget}")
    
    if remaining_budget > 0:
        print("You have a surplus! Consider saving this.")
    elif remaining_budget < 0:
        print("You are over budget! Review your expenses.")
    else:
        print("Your budget is perfectly balanced.")

# Run the program
if __name__ == "__main__":
    calculate_budget()
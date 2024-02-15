import datetime
import matplotlib.pyplot as plt

class ExpenseTracker:
    expenses = []
    budgets = {}
    reminders = {}

    # Expense Logging
    def log_expense(self, amount, category, date=None):
        if date is None:
            date = datetime.datetime.now()
        self.expenses.append((date, amount, category))
    
    # Budget Setting
    def set_budget(self, category, budget_amount):
        self.budgets[category] = budget_amount
    
    # Reminder Setting
    def set_reminder(self, reminder_name, reminder_date):
        self.reminders[reminder_name] = reminder_date
    
    # Checking and Displaying Budget
    def check_budget(self):
        print(f"Total Budget Remain: ")
        for category, budget_amount in self.budgets.items():
            total_expense = sum(amount for _, amount, cat in self.expenses if cat == category)
            if total_expense > budget_amount:
                print(f"{category}: You have exceeded your budget {budget_amount} by {total_expense - budget_amount}.")
                continue
            else:
                print(f"{category}: {budget_amount - total_expense}")
    
    # Displaying Expense History
    def show_expense_history(self):
        print("Expense History:")
        for date, amount, category in self.expenses:
            print(f"Date: {date}, Amount: {amount}, Category: {category}")
    
    # Visualization of Expenses
    def visualize_expenses(self):
        categories = {}
        for _, amount, category in self.expenses:
            if category not in categories:
                categories[category] = 0
            categories[category] += amount

        plt.bar(categories.keys(), categories.values())
        plt.xlabel('Categories')
        plt.ylabel('Amount Spent')
        plt.title('Expense Visualization')
        plt.show()
    
    # Checking and Displaying Reminders
    def check_reminders(self):
        today = datetime.datetime.now().date()
        for reminder_name, reminder_date in self.reminders.items():
            if today == reminder_date:
                print(f"Don't forget: {reminder_name} is due today!")
                continue
            else:
                print(f"Don't forget: {reminder_name} is due on {reminder_date}!")
        for category, budget_amount in self.budgets.items():
            total_expense = sum(amount for _, amount, cat in self.expenses if cat == category)
            if total_expense >= 0.8 * budget_amount:
                print(f"Warning! You are approaching your budget limit for {category}. Budget remaining: {budget_amount}.")

tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Log Expense")
    print("2. Set Budget")
    print("3. Set Reminder")
    print("4. Show Expense History")
    print("5. Visualize Expenses")
    print("6. Check Budget")
    print("7. Check Reminders")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            tracker.log_expense(amount, category)
        except ValueError:
            print("Invalid Expense Amount! Please enter valid expense amount.")

    elif choice == '2':
        try:
            category = input("Enter the category for budget: ")
            budget_amount = float(input("Enter the budget amount: "))
            tracker.set_budget(category, budget_amount)
        except ValueError:
            print("Invalid Budget Amount! Please enter valid budget amount.")

    elif choice == '3':
        try:
            reminder_name = input("Enter the reminder name: ")
            reminder_date = input("Enter the reminder date (YYYY-MM-DD): ")
            reminder_date = datetime.datetime.strptime(reminder_date, '%Y-%m-%d').date()
            tracker.set_reminder(reminder_name, reminder_date)
        except ValueError:
            print("Invalid Date! Please enter valid date in (YYYY-MM-DD) format.")

    elif choice == '4':
        tracker.show_expense_history()

    elif choice == '5':
        tracker.visualize_expenses()

    elif choice == '6':
        tracker.check_budget()

    elif choice == '7':
        tracker.check_reminders()

    elif choice == '8':
        print("Exiting...\nThank You!!!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

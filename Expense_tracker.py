def add_expense():
    amount = input("Enter the expense amount: ")
    category = input("Enter the expense category (like food, travel, shopping, etc.): ")

    with open("expenses.txt", "a") as file:  
        file.write(amount + "," + category + "\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            data = file.readlines()

        print("\nYour Expenses")
        for line in data:
            amount, category = line.strip().split(",")
            print("Rs", amount, "Category:", category)
        print()
    except:
        print("No expenses found.")


def total_expenses():
    try:
        with open("expenses.txt", "r") as file:
            data = file.readlines()

        total = 0
        for line in data:
            amount, category = line.strip().split(",")
            total += float(amount)

        print("\nTotal expenses: Rs", total)
        print()
    except:
        print("No expenses found.")


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

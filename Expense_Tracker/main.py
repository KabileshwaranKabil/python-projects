# Main.py 

from expensetracker import ExpenseTracker

expenseTracker = ExpenseTracker()
while True:
	try:
		print("\nExpense Tracker")
		print("---------------")

		choice = int(input("1.Add Expense\n2.View Expenses\n3.Exit\n:-"))
		match choice:
			case 1:
				expenseTracker.add_expense()
			case 2:
				expenseTracker.view_all_expenses()
			case 3:
				print("\nThank you!")
				break
			case _:
				print("please enter 1-3")
	except ValueError:
		print("oops! please enter a number, not a word")


# Expense Tracker
from expense import Expense 
import json

class ExpenseTracker:
	def __init__(self):
		self.expenses = []

	def store_expense(self):
		try:
			with open("expenses.json","w") as f:
				json.dump([exp.__dict__ for exp in self.expenses],f,indent=4)
		except PermissionError:
			print("Permission denied.")


	def load_expenses(self):
		try:
			with open("expenses.json","r") as f:
				data = json.load(f)
				self.expenses = [Expense(**item) for item in data]
		except FileNotFoundError:
			print("No saved expenses yet.")
		except json.JSONDecodeError:
			print("File is empty or corrupted")
			self.expenses=[]


	def add_expense(self):
		try:
			amount = float(input("Amount: "))
			category = input("Category: ")
			description = input("Description: ")
			exp = Expense(amount,category,description)
			self.expenses.append(exp)
			self.store_expense()
			print("successfully added to record!\n")
		except ValueError:
			print("oops! please enter correct values")



	def view_all_expenses(self):
		print("\n-- Expenses --")
		self.load_expenses()
		if not self.expenses:
			print("No Expenses recorded yet.")
		else:
			for expense in self.expenses:
				print(expense)



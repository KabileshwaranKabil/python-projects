# Expense 

class Expense:
	def __init__(self,amount,category,description):
		self.amount = amount
		self.category = category
		self.description = description

	def __str__(self):
		return f"Amount: {self.amount} | Category: {self.category} | Description: {self.description}"


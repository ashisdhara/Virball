class User:
	def __init__(self, name, email, password, points, budget):
		self.name = name
		self.email = email
		self.password = password
		self.points = points
		self.budget = budget
	
	def store_new_user(self):
		pass
	
	def fetch_user_by_id(self, user_id):
		pass

	def add_user_points(self, added_points):
		pass

	def decrease_user_budget(self, budget_decrement):
		pass

	def increase_user_budget(self, budget_increment):
		pass

	
	

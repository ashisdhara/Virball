import models.user_model

class User:
	def __init__(self, name, email, password, points, budget):
		self.name = name
		self.email = email
		self.password = password
		self.points = points
		self.budget = budget
	
	def store_new_user(self):
		models.user_model.create_user(self.name, self.email, self.password)
		
	@staticmethod
	def get_user_by_id(user_id):
		user_data = {}
		user_data = models.user_model.fetch_details_by_id(user_id)
		
		return User(user_data['name'], user_data['email'], user_data['password'], user_data['points'], user_data['budget'])

	def add_user_points(self, added_points):
		self.points += added_points

	def decrease_user_budget(self, budget_decrement):
		self.budget -= budget_decrement

	def increase_user_budget(self, budget_increment):
		self.bubdget += budget_increment

	
	

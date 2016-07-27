import models.user_model
import entities.Player

class User:
	def __init__(self, user_id, name, email, password, points, budget):
		self.id = user_id
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
		
		return User(user_data['id'],user_data['name'], user_data['email'], user_data['password'], user_data['points'], user_data['budget'])

	def add_user_points(self, added_points):
		self.points += added_points
		models.user_model.update_user_points(self.id, self.points)

	def decrease_user_budget(self, budget_decrement):
		self.budget -= budget_decrement
		models.user_model.update_user_budget(self.id, self.budget)

	def increase_user_budget(self, budget_increment):
		self.budget += budget_increment
		models.user_model.update_user_budget(self.id, self.budget)
		
	def check_player_add(self, player ):
		if(player.value > self.budget):
			return 0
		else:
			return 1
	
	def add_player (self, player):
		models.user_model.add_player(self.id, player.name)
		self.decrease_user_budget(player.value)
		models.user_model.update_user_budget(self.id, self.budget)
		return
	
	def remove_player(self, player):
		models.user_model.remove_player(self.id,player.name )
		self.increase_user_budget( player.value)
		models.user_model.update_user_budget(self.id, self.budget)
		
	

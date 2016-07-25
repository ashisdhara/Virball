
class Player:
	
	def __init__(self, name, value, goals, yellow, red, status, team, games, score):
		self.name = name
		self.value = value
		self.goals = goals
		self.yellow = yellow
		self.red = red
		self.status = status
		self.team = team
		self.games = games
		self.score = score

	def store_new_player(self):
		pass

	def fetch_player_by_id(self):
		pass

	def played_game(self):
		self.games += 1

	def got_red(self):
		self.red += 1

	def got_yellow(self, yellows):
		self.yellow += yellows

	def change_status(self, new_status):
		self.status = new_status

	def got_goal(self, goals):
		self.goals += goals

	def changed_value(self, change_value):
		self.value += change_value

	

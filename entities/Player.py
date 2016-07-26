import models.player_model

class Player(object):
	
	def __init__(self, name, position, value, team, status, goals, yellow, red, games, score):
		self.name = name
		self.position = position
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
	
	@staticmethod
	def get_player_by_name(player_name):
		raw_player = models.player_model.get_player_by_name(player_name)
		new_player = Player(raw_player[1],raw_player[2], raw_player[3], raw_player[4], raw_player[5], raw_player[6], raw_player[7], raw_player[8], raw_player[9], raw_player[11],)
		return new_player
	
	
	@staticmethod	
	def get_selected_players(user_id):
		raw_players = models.player_model.get_players_by_user_id(user_id)
		user_players_list = []
		for raw_player in raw_players:
			user_players_list.append(Player(raw_player[1],raw_player[2], raw_player[3], raw_player[4], raw_player[5], raw_player[6], raw_player[7], raw_player[8], raw_player[9], raw_player[11],))
		return user_players_list

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

	

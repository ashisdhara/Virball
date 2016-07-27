import models.player_model

class Player(object):
	
	def __init__(self, name, position, value, team, status, goals, yellow, red, games,clean_sheets, score, assists):
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
		self.assists = assists
		self.clean_sheets = clean_sheets

	def store_new_player(self):
		pass

	def fetch_player_by_id(self):
		pass
	
	@staticmethod
	def get_player_by_name(player_name):
		raw_player = models.player_model.get_player_by_name(player_name)
		new_player = Player(raw_player[1],raw_player[2], raw_player[3], raw_player[4], raw_player[5], raw_player[6], raw_player[7], raw_player[8], raw_player[9],raw_player[10], raw_player[11], raw_player[12])
		return new_player
	
	
	@staticmethod	
	def get_selected_players(user_id):
		raw_players = models.player_model.get_players_by_user_id(user_id)
		user_players_list = []
		for raw_player in raw_players:
			user_players_list.append(Player(raw_player[1],raw_player[2], raw_player[3], raw_player[4], raw_player[5], raw_player[6], raw_player[7], raw_player[8], raw_player[9],raw_player[10], raw_player[11], raw_player[12]))
		return user_players_list

	def played_game(self):
		self.score += 2
		self.games += 1
		self.update_users_points(2)

	def got_red(self):
		self.score -= 3
		self.value -= 0.2
		self.red += 1
		self.update_users_points(-3)

	def got_yellow(self, yellows):
		self.score -= yellows*1
		self.value -= 0.1
		self.yellow += yellows
		self.update_users_points(-1)

	def change_status(self, new_status):
		self.status = new_status

	def got_clean_sheet(self):
		self.score += 3
		self.value += 0.1
		self.clean_sheets += 1
		self.update_users_points(3)

	def got_goal(self, goals):
		self.score += 5
		self.value += 0.1
		self.goals += goals
		self.update_users_points(5)

	def got_assist(self, assists):
		self.score += 3
		self.assists += assists
		self.update_users_points(3)

	def changed_value(self, change_value):
		self.value += change_value

	def persist_player(self):
		models.player_model.update_player(self.name, self.value, self.goals, self.yellow, self.red, self.score)
		
	def update_users_points(self, score_change):
		models.player_model.update_users_points(self.name, score_change)

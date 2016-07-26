import models.player_model
import entities.Player 


class Forward (entities.Player.Player):
	def __init__(self, name, value, goals, yellow, red, status, team, clean_sheets, games, score):
		Player.__init__(self, name, value, goals, assists, yellow, red, status, team, games, score)		
		
	def store_new_player(self):
		pass	

	def fetch_player_by_id(self):
		pass

	@staticmethod	
	def get_unselected_players(user_id):
		raw_players = models.player_model.get_unselected_players(user_id, "fwd")
		user_unselected_players_list = []
		for raw_player in raw_players:
			user_unselected_players_list.append(entities.Player.Player(raw_player[1],raw_player[2], raw_player[3], raw_player[4], raw_player[5], raw_player[6], raw_player[7], raw_player[8], raw_player[9], raw_player[11],))
		return user_unselected_players_list


	def played_game(self):
		self.score += 2
		self.games += 1

	def got_red(self):
		self.score -= 3
		self.value -= 0.1
		self.red += 1

	def got_yellow(self, yellows):
		self.score -= yellows*1
		self.value -= 0.1
		self.yellow += yellows

	def change_status(self, new_status):
		self.status = new_status


	def got_goal(self, goals):
		self.score += 4
		self.value += 0.1
		self.goals += goals

	def got_assist(self, assists):
		self.score += 3
		self.value += 0.1
		self.assists += assists

	def changed_value(self, change_value):
		self.value += change_value


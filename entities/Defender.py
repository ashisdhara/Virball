

class Defender (Player):
	def __init__(self, name, value, goals, yellow, red, status, team, clean_sheets, games, score):
		Player.__init__(self, name, value, goals, assists, yellow, red, status, team, games, score)		
		self.clean_sheets = clean_sheets
		
	def store_new_player(self):
		pass	

	def fetch_player_by_id(self):
		pass
	
	def played_game(self):
		self.score += 2
		self.games += 1

	def got_red(self):
		self.score -= 3
		self.value -= 0.2
		self.red += 1

	def got_yellow(self, yellows):
		self.score -= yellows*1
		self.value -= 0.1
		self.yellow += yellows

	def change_status(self, new_status):
		self.status = new_status

	def got_clean_sheet(self):
		self.score += 3
		self.value += 0.1
		clean_sheets += 1

	def got_goal(self, goals):
		self.score += 5
		self.value += 0.1
		self.goals += goals

	def got_assist(self, assists):
		self.score += 3
		self.assists += assists

	def changed_value(self, change_value):
		self.value += change_value


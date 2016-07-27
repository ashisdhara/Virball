import urllib
import json
import sys
import controllers.Score_Parser 
import entities.Player 


class Local_Score_Parser (controllers.Score_Parser.Score_Parser):
	def __init__(self):
		Score_Parser.__init__()
		return
		

	@staticmethod
	def fetch_games():
		with open('test2.json') as data_file:    
			data = json.load(data_file)
			# data['games'][0]['assist']
			for i in range(len(data['games'])):
				for j in range(len(data['games'][i]['goals'])):
					player_name = data['games'][i]['goals'][j]
					curr_player = entities.Player.Player.get_player_by_name(player_name)
					curr_player.got_goal(1)
					curr_player.persist_player()
				 	
				for j in range(len(data['games'][i]['assist'])):
				 	player_name = data['games'][i]['assist'][j]
				 	curr_player = entities.Player.Player.get_player_by_name(player_name)
				 	curr_player.got_assist(1)
				 	curr_player.persist_player()
				 	
				for j in range(len(data['games'][i]['yellow'])):
					player_name = data['games'][i]['yellow'][j]
				 	curr_player = entities.Player.Player.get_player_by_name(player_name)
				 	curr_player.got_yellow(1)
				 	curr_player.persist_player()
				 	
				for j in range(len(data['games'][i]['red'])):
				 	player_name = data['games'][i]['red'][j]
				 	curr_player = entities.Player.Player.get_player_by_name(player_name)
				 	curr_player.got_red()
				 	curr_player.persist_player()
				 	
				for j in range(len(data['games'][i]['clean_sheet'])):
				 	player_name = data['games'][i]['clean_sheet'][j]
				 	curr_player = entities.Player.Player.get_player_by_name(player_name)
 		  			curr_player.got_clean_sheet()
 		  			curr_player.persist_player()
 		  		return 1


	def get_date():
		pass
		

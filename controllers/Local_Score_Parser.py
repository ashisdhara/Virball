import urllib
import json
import sys
from pprint import pprint
import controllers.Score_Parser as score_parser 


class Local_Score_Parser (Score_Parser):
	def __init__(self):
		Score_Parser.__init__()
		pass
		

	@staticmethod
	def fetch_games():
		with open('test2.json') as data_file:    
			data = json.load(data_file)
			


	def get_date():
		pass
		
Local_Score_Parser.fetch_games()

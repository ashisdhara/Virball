from flask import Flask, render_template, request, jsonify
import models.db_config

def get_players_by_user_id(user_id):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "SELECT *  from players  join users_players on players.id = users_players.player_id where users_players.user_id=" + str(user_id) + ";"
	cursor.execute(query)
	raw_players = cursor.fetchall()
	return raw_players
		
def get_unselected_players(user_id, pos):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "SELECT *  from players  where players.id not in (select players.id from players join users_players on players.id = users_players.player_id where users_players.user_id = "+ str(user_id)+");"
	cursor.execute(query)
	raw_players = cursor.fetchall()
	return raw_players

def get_player_by_name(player_name):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "SELECT *  from players  where name='"+ player_name+"' ;"
	cursor.execute(query)
	raw_player = cursor.fetchone()
	return raw_player

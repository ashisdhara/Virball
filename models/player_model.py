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
	
def update_player(name, value, goals, yellow, red, score):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "update players set value = "+ str(value)+", goals = "+ str(goals)+", yellow = "+str(yellow)+", red= "+ str(red) +", score = "+str(score)+" where name = '"+ name+"';"
	cursor.execute(query)
	con.commit()
	return 1

def update_users_points(player_name, score_change):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "update users set points = points + "+ str(score_change)+" where id in (select distinct user_id from users_players join players on users_players.player_id = players.id where players.name = '"+player_name+"') ;"
	cursor.execute(query)
	con.commit()
	return 1
	
def get_top_players(count):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "SELECT name, score  from players order by score desc LIMIT "+ str(count) +";"
	cursor.execute(query)
	leaderboard_data = cursor.fetchall()
	return leaderboard_data	


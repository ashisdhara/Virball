from flask import Flask, render_template, request, jsonify
import models.db_config

def get_players_by_user_id(user_id):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "SELECT *  from players  join users_players on players.id = users_players.player_id where users_players.user_id=" + str(user_id) + ";"
	cursor.execute(query)
	raw_players = cursor.fetchall()
	return raw_players
		


from flask import Flask, render_template, request, session
import models.user_model
import entities.User
import entities.Goalkeeper
import entities.Defender
import entities.Midfielder
import entities.Forward
import entities.Player

def team_edit():
	if session['user_id'] is not None :
		user_id = int(session['user_id'])
		selected_players = entities.Player.get_selected_players(user_id)
		return render_template('team_remove.html', players = selected_players)
	else :
		return render_template('login.html')
	
def team_add():
	if session['user_id'] is not None :
		user_id = session['user_id']
		unselected_goalkeepers_list =  entities.Goalkeeper.Goalkeeper.get_unselected_players(user_id)
		unselected_defenders_list =  entities.Defender.Defender.get_unselected_players(user_id)
		unselected_midfielders_list =  entities.Midfielder.Midfielder.get_unselected_players(user_id)
		unselected_forwards_list =  entities.Forward.Forward.get_unselected_players(user_id)
		return render_template('team_add.html', goalkeepers = unselected_goalkeepers_list, defenders = unselected_defenders_list, midfielders =unselected_midfielders_list, forwards =unselected_forwards_list  )
	else :
		return render_template('login.html')

def team_add_submit():
	if session['user_id'] is not None :
		curr_user = entities.User.User.get_user_by_id(session['user_id'])
		_add_player_name = str(request.form['player_name'])
		new_player = entities.Player.Player.get_player_by_name(_add_player_name)
		addable = curr_user.check_player_add(new_player) 
		if addable != 0:
			curr_user.add_player(new_player)
			team_add()
		else :
			return "Player Not Addable"

def team_remove():
	if session['user_id'] is not None :
		user_id = session['user_id']
		selected_players_list =  entities.Player.Player.get_selected_players(user_id)
		return render_template('team_remove.html', players = selected_players_list)
	else :
		return render_template('login.html')
			
def team_remove_submit():
	if session['user_id'] is not None :
		curr_user = entities.User.User.get_user_by_id(session['user_id'])
		_remove_player_name = str(request.form['player_name'])
		new_player = entities.Player.Player.get_player_by_name(_remove_player_name)
		curr_user.remove_player(new_player)
		team_remove()
	else :
			return "Player Not Addable"


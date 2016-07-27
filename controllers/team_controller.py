from flask import Flask, render_template, request, session, redirect
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
		curr_user = entities.User.User.get_user_by_id(session['user_id'])
		unselected_goalkeepers_list =  entities.Goalkeeper.Goalkeeper.get_unselected_players(user_id)
		return render_template('team_add.html', goalkeepers = unselected_goalkeepers_list, curr_user = curr_user)
	else :
		return render_template('login.html')

def team_add_submit():
	if session['user_id'] is not None :
		curr_user = entities.User.User.get_user_by_id(session['user_id'])
		_add_player_name = str(request.form['player_name'])
		new_player = entities.Player.Player.get_player_by_name(_add_player_name)
		addable = curr_user.check_player_add(new_player)
		count = models.user_model.get_player_count(curr_user.id)
		error_message = "Cannot Add the Player"
		if addable != 0 and count<11:
			curr_user.add_player(new_player)
			return redirect("/team_add", code=302)
		else :
			return render_template("error.html", error_message = error_message)

def team_remove():
	if session['user_id'] is not None :
		user_id = session['user_id']
		curr_user = entities.User.User.get_user_by_id(session['user_id'])
		selected_players_list =  entities.Player.Player.get_selected_players(user_id)
		return render_template('team_remove.html', players = selected_players_list, curr_user = curr_user)
	else :
		return render_template('login.html')
			
def team_remove_submit():
	if session['user_id'] is not None :
		curr_user = entities.User.User.get_user_by_id(session['user_id'])
		_remove_player_name = str(request.form['player_name'])
		new_player = entities.Player.Player.get_player_by_name(_remove_player_name)
		curr_user.remove_player(new_player)
		return redirect("/team_remove", code=302)
	else :
		error_message = "Cannot Remove the Player"
		return render_template("error.html", error_message = error_message)


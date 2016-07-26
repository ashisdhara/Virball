from flask import Flask, render_template, request, session
import models.user_model
import entities.User
import entities.Goalkeeper
import entities.Defender
import entities.Midfielder
import entities.Forward

def team_edit():
	if session['user_id'] is not None :
		user_id = int(session['user_id'])
		goalkeepers = entities.Goalkeeper.get_players(user_id)
		defenders = entities.Defender.get_players(user_id)
		midfielders = entities.Midfielder.get_players(user_id)
		forwawrds = entities.Forward.get_players(user_id)
		return render_template('team_edit.html', goalkeepers= goalkeepers, defenders= defenders, midfielders= midfielders, forwards = forwards)
	else return render_template('login.html')

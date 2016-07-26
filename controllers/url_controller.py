from flask import Flask, render_template, session,request
import controllers.login_controller
import controllers.signup_controller
import models.user_model
import entities.User as user
import entities.Player as player


def url_label(label_name):
	if "login" in label_name:
		return  getattr(controllers.login_controller, label_name)()
	if "signup" in label_name:
		return getattr(controllers.signup_controller, label_name) ()
	if "team" in label_name:
		return getattr(controllers.team_controller, label_name) ()
	if "car" in label_name:
		print str(request.form['car_name'])
	if "show" in label_name:
		return render_template("edit_team.html")
	
def root_url():
	if "user_id" in session:
		user_id = session['user_id']
		curr_user = user.User.get_user_by_id(user_id)
		user_players = []
		user_players = player.Player.get_players_by_user_id(user_id)
#		user_data = models.user_model.fetch_details_by_id(user_id)
		return render_template('home.html', curr_user = curr_user, user_players = user_players)
	else:	
		return render_template('login.html') 


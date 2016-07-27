from flask import Flask, render_template, session,request
import controllers.login_controller
import controllers.signup_controller
import controllers.team_controller
import controllers.update_controller
import controllers.leaderboard_controller
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
	if "update" in label_name:
		return getattr(controllers.update_controller, label_name)()
	if "leaderboard" in label_name:
		return getattr(controllers.leaderboard_controller, label_name)()
		
	
def root_url():
	if "user_id" in session:
		user_id = session['user_id']
		curr_user = user.User.get_user_by_id(user_id)
		user_players = []
		user_players = player.Player.get_selected_players(user_id)
#		user_data = models.user_model.fetch_details_by_id(user_id)
		return render_template('home.html', curr_user = curr_user, user_players = user_players)
	else:	
		return render_template('login.html') 


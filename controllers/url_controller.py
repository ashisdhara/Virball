from flask import Flask, render_template, session
import controllers.login_controller
import controllers.signup_controller
import models.user_model


def url_label(label_name):
	if "login" in label_name:
		return  getattr(controllers.login_controller, label_name)()
	if "signup" in label_name:
		return getattr(controllers.signup_controller, label_name) ()
	
def root_url():
	if "user_id" in session:
		user_id = session['user_id']
		user_data = models.user_model.fetch_details_by_id(user_id)
		return render_template('home.html', entries=user_data)
	else:	
		return render_template('login.html') 


from flask import Flask, render_template, request
import models.user_model

def signup():
	return render_template('signup.html')
	
def signup_complete():	
	_email = str(request.form['inputEmail'])
	_name = str(request.form['inputName'])
	_password = str(request.form['inputPassword'])
	models.user_model.create_user(_name, _email, _password)
	return render_template('login.html')

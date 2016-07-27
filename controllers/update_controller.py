from flask import Flask, render_template, request, session
import models.user_model
import entities.User
import controllers.Local_Score_Parser

def update():
	if session['user_id'] == 1 :
		controllers.Local_Score_Parser.Local_Score_Parser.fetch_games()
		return render_template('update_success.html')
	else :
		return "Not Authorized to view this page"

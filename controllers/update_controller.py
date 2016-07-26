from flask import Flask, render_template, request, session
import models.user_model
import entities.User

def update():
	if session['user_id'] == 1 :
		return 1
	else :
		return 0

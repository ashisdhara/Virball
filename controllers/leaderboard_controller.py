from flask import Flask, render_template, request
import models.user_model

def leaderboard():
	top_user_scores = models.user_model.get_top_user_scores(5)
	
	return render_template('leaderboard.html')
	


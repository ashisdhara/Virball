from flask import Flask, render_template, request
import models.user_model
import models.player_model

def leaderboard():
	top_user_scores = models.user_model.get_top_user_scores(5)
	top_footballers = models.player_model.get_top_players(5)
	return render_template('leaderboard.html', top_users = top_user_scores, top_players = top_footballers)
	


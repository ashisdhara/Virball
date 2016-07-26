from flask import Flask, render_template, request, jsonify
import models.db_config

def create_user(name, email, password):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "Insert into users (name, email, password, points, budget) values ('"+ name +"', '"+ email +"','"+ password+"',0,100);"
	cursor.execute(query)
	con.commit()
	return 1

def get_user(email, password):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "SELECT id from users where email='" + email + "' and password='" + password + "';"
	cursor.execute(query)
	data = cursor.fetchall()
	if data is None :
		return ""
	else:
		return data[0][0]
		
def fetch_details_by_id(user_id):
	con = models.db_config.create_connection()
	cursor = con.cursor()
	query = "SELECT * from users where id=" + str(user_id) + ";"
	cursor.execute(query)
	data = cursor.fetchone()
	
	if data is None :
		return ""
	else:
		user_data = {}
		user_data['id'] = data[0]
		user_data['name'] = data[1]		
		user_data['email'] = data[2]
		user_data['password'] = data[3]
		user_data['points'] = data[4]
		user_data['budget'] = data[5]
		return user_data
		

	

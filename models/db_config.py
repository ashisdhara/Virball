from flask import Flask, render_template, request
from flask.ext.mysql import MySQL

def create_connection():
	mysql = MySQL()
	app = Flask(__name__)
	app.config['MYSQL_DATABASE_USER'] = 'root'
	app.config['MYSQL_DATABASE_PASSWORD'] = ''
	app.config['MYSQL_DATABASE_DB'] = 'virball'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'
	mysql.init_app(app)
	con = mysql.connect()
	return con

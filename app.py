from flask import Flask, render_template
from flask.ext.mysql import MySQL
import controllers.controller1
import controllers.url_controller

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'fantasy_foot'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
##	con = mysql.connect()
##	cursor = con.cursor()
##	cursor.execute("Insert into new_table (id,name) values (1, 'Ashis');")
##	con.commit()
	return render_template('login.html') 
    
@app.route("/<label_name>")
def label_redirect(label_name):
	response = controllers.url_controller.url_label(label_name)
	return response

@app.route('/<label_name>', methods=['POST'])
def input_redirect(label_name):
	_name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
	response = controllers.url_controller.url_post(label_name)
	return response

if __name__ == "__main__":
    app.run()

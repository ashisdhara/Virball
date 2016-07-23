from flask import Flask, render_template
from flask.ext.mysql import MySQL

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
	return render_template('index.html') 
    
if __name__ == "__main__":
    app.run()

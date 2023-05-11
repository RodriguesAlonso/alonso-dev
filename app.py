import pymysql
from flask import Flask, render_template, flash, request, redirect
from flask_bootstrap import Bootstrap5
from flaskext.mysql import MySQL


app = Flask(__name__)
app.secret_key = "chave"

bootstrap = Bootstrap5(app)


app.config['MYSQL_DATABASE_USER'] = "mysql://root:WLGXoVnRJaIRJnYZeK9W@containers-us-west-158.railway.app:6991/railway"
app.config['MYSQL_DATABASE_PASSWORD'] = "WLGXoVnRJaIRJnYZeK9W"
app.config['MYSQL_DATABASE_DB'] = "railway"
app.config['MYSQL_DATABASE_HOST'] = "containers-us-west-158.railway.app"

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tag')
def tag():
    return render_template('tags.html')

@app.route('/test', methods = ["GET"])
def test():
    conn = mysql.connect()
    my_cursor = conn.cursor()
    my_cursor.execute("SELECT * FROM todo")            
    rows = my_cursor.fetchall()    
    print(rows)
    
    
if __name__ == '__main__':
    app.run()
    
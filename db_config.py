from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = "mysql://root:WLGXoVnRJaIRJnYZeK9W@containers-us-west-158.railway.app:6991/railway"
app.config['MYSQL_DATABASE_PASSWORD'] = "WLGXoVnRJaIRJnYZeK9W"
app.config['MYSQL_DATABASE_DB'] = "railway"
app.config['MYSQL_DATABASE_HOST'] = "containers-us-west-158.railway.app"

 
 \mysql.init_app(app)
from flask import Flask
from flask_mysqldb import MySQL
from routes import cargarRutas
from config import Config



app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)
app.mysql = mysql
cargarRutas(app)


app.run(debug=True, port=4000, host='0.0.0.0')


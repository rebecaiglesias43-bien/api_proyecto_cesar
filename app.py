import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mysqldb import MySQL

from config import Config
from routes import cargarRutas

app = Flask(__name__)
app.config.from_object(Config)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or os.getenv('SECRET_KEY') or 'change-me'

CORS(app)
JWTManager(app)

mysql = MySQL(app)
app.mysql = mysql

cargarRutas(app)
app.run(debug=True, port=4000, host='0.0.0.0')

# app.py
from flask import Flask
from flask_mysqldb import MySQL

import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from routes import cargarRutas  # Cambiado: cargarRuta → cargarRutas
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or 'change-me'
CORS(app)
JWTManager(app)

mysql = MySQL(app)
app.mysql = mysql
cargarRutas(app)  # Cambiado: cargarRuta → cargarRutas
app.run(debug=True, port=4000, host='0.0.0.0')
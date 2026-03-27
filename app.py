from flask import Flask
from flask_mysqldb import MySQL
from routes import cargarRutas
from config import Config
from rutas.item_rutas import item_bp

app = Flask(__name__)

app.config.from_object(Config)

mysql = MySQL(app)
app.mysql = mysql

app.register_blueprint(item_bp)

cargarRutas(app)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')

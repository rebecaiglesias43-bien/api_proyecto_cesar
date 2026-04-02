from flask import current_app
from models.cliente_model import Cliente

def listado_cliente():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM clientes"
    c.execute(sql)
    datos = c.fetchall()
    return datos

def registro():
    return

def editar():
    return

def eliminar():
    return

def buscarxcodigo():
    return
from flask import jsonify, request
from services.cliente_services import listado_cliente

def cntlistado():
    datos = listado_cliente()
    print(datos)

    
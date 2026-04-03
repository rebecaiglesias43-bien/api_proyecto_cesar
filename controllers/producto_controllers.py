from flask import request, jsonify, current_app
from services.producto_services import ProductoService

def cntlistado_productos():
    service = ProductoService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntobtener_producto(id_producto):
    service = ProductoService(current_app.mysql)
    producto = service.obtener_por_id(id_producto)
    if producto:
        return jsonify(producto)
    return jsonify({'error': 'Producto no encontrado'}), 404

def cntcrear_producto():
    data = request.get_json()
    service = ProductoService(current_app.mysql)
    producto = service.crear(
        nombre=data.get('nombre'),
        precio=data.get('precio'),
        stock=data.get('stock', 0),
        estado=data.get('estado', 'activo')
    )
    return jsonify(producto), 201
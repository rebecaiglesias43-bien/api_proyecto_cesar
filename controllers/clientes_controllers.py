from flask import request, jsonify, current_app
from services.clientes_services import ClienteService

def cntlistado_clientes():
    service = ClienteService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntobtener_cliente(id_cliente):
    service = ClienteService(current_app.mysql)
    cliente = service.obtener_por_id(id_cliente)
    if cliente:
        return jsonify(cliente)
    return jsonify({'error': 'Cliente no encontrado'}), 404

def cntcrear_cliente():
    data = request.get_json()
    service = ClienteService(current_app.mysql)
    cliente = service.crear(
        id_usuarioFK=data.get('id_usuarioFK'),
        nombre=data.get('nombre'),
        apellido=data.get('apellido'),
        telefono=data.get('telefono'),
        direccion=data.get('direccion')
    )
    return jsonify(cliente), 201
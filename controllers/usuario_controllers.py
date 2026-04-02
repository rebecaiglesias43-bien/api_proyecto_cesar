from flask import request, jsonify, current_app
from services.usuario_services import UsuarioService

def cntlistado_usuarios():
    service = UsuarioService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntobtener_usuario(id_usuario):
    service = UsuarioService(current_app.mysql)
    usuario = service.obtener_por_id(id_usuario)
    if usuario:
        return jsonify(usuario)
    return jsonify({'error': 'Usuario no encontrado'}), 404

def cntcrear_usuario():
    data = request.get_json()
    service = UsuarioService(current_app.mysql)
    usuario = service.crear(
        username=data.get('username'),
        password=data.get('password'),
        email=data.get('email'),
        rol=data.get('rol', 'cliente'),
        estado=data.get('estado', 'activo')
    )
    return jsonify(usuario), 201
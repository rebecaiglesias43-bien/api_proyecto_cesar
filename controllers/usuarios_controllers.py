from flask import current_app, jsonify, request
from flask_jwt_extended import create_access_token

from services.usuarios_services import UsuarioService

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
    data = request.get_json(silent=True) or {}
    service = UsuarioService(current_app.mysql)
    usuario = service.crear(
        username=data.get('username'),
        password=data.get('password'),
        email=data.get('email'),
        rol=data.get('rol', 'cliente'),
        estado=data.get('estado', 'activo')
    )
    return jsonify(usuario), 201

def cntlogin_usuario():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')

    if not isinstance(username, str) or not username.strip():
        return jsonify({'error': 'El campo "username" es requerido'}), 400
    if not isinstance(password, str) or not password:
        return jsonify({'error': 'El campo "password" es requerido'}), 400

    service = UsuarioService(current_app.mysql)
    usuario = service.autenticar(username.strip(), password)
    if not usuario:
        return jsonify({'error': 'Credenciales invalidas'}), 401

    token = create_access_token(
        identity=str(usuario['id_usuario']),
        additional_claims={
            'username': usuario['username'],
            'rol': usuario['rol'],
            'estado': usuario['estado']
        }
    )
    return jsonify({
        'access_token': token,
        'usuario': usuario
    })

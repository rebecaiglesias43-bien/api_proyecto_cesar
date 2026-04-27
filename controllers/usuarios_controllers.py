from flask import request, jsonify, current_app
from services.usuarios_services import UsuarioService
def validar_datos_usuario(data):
    user = data.get('username')
    email = data.get('email')
    passw = data.get('password')

    if not user or not email or not passw:
        return False, 'Username, email y password son obligatorios'
    
    if len(str(passw)) < 8:
        return False, 'La contraseña debe tener al menos 8 caracteres'

    cur = current_app.mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE usu_username = %s OR usu_email = %s", (user, email))
    if cur.fetchone():
        cur.close()
        return False, 'El nombre de usuario o el correo ya están registrados'
    
    cur.close()
    return True, None
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
    es_valido, mensaje = validar_datos_usuario(data)
    if not es_valido:
        return jsonify({'error': mensaje}), 400
    service = UsuarioService(current_app.mysql)
    usuario = service.crear(
        username=data.get('username'),
        password=data.get('password'),
        email=data.get('email'),
        rol=data.get('rol', 'cliente'),
        estado=data.get('estado', 'activo')
    )
    return jsonify(usuario), 201
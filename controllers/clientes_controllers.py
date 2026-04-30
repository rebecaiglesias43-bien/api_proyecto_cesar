from flask import request, jsonify, current_app
from services.clientes_services import ClienteService
from flask_jwt_extended import jwt_required

def validar_datos_cliente(data):
    id_usuario = data.get('id_usuarioFK')
    nombre = data.get('nombre')
    
    if not id_usuario or not nombre:
        return False, 'Falta el ID de usuario o el nombre'
    
    cur = current_app.mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE usu_id = %s", (id_usuario,))
    if not cur.fetchone():
        cur.close()
        return False, 'Ese usuario no existe'
    
    cur.close()
    return True, None

@jwt_required()

def cntlistado_clientes():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except (TypeError, ValueError):
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser números enteros'}), 400

    if page <= 0 or per_page <= 0:
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser mayores que cero'}), 400

    service = ClienteService(current_app.mysql)
    return jsonify(service.listar_todos(page, per_page))

@jwt_required()
def cntobtener_cliente(id_cliente):
    service = ClienteService(current_app.mysql)
    cliente = service.obtener_por_id(id_cliente)
    if cliente:
        return jsonify(cliente)
    return jsonify({'error': 'Cliente no encontrado'}), 404

@jwt_required()
def cntcrear_cliente():
    data = request.get_json()

    es_valido, mensaje = validar_datos_cliente(data)
    if not es_valido:
        return jsonify({'error': mensaje}), 400

    service = ClienteService(current_app.mysql)
    cliente = service.crear(
        id_usuarioFK=data.get('id_usuarioFK'),
        nombre=data.get('nombre'),
        apellido=data.get('apellido'),
        telefono=data.get('telefono'),
        direccion=data.get('direccion')
    )
    return jsonify(cliente), 201
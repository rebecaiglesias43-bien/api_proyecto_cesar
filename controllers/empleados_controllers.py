from flask import request, jsonify, current_app
from services.empleados_services import EmpleadoService
def validar_datos_empleado(data):
    id_usuario = data.get('id_usuario')
    nombre = data.get('nombre')
    cargo = data.get('cargo')

    if not id_usuario or not nombre or not cargo:
        return False, 'Faltan campos obligatorios (ID, nombre o cargo)'
    
    cur = current_app.mysql.connection.cursor()

    cur.execute("SELECT * FROM usuarios WHERE usu_id = %s", (id_usuario,))
    if not cur.fetchone():
        cur.close()
        return False, 'Ese usuario no existe en el sistema'


    cur.execute("SELECT * FROM empleados WHERE emp_usuario_id = %s", (id_usuario,))
    if cur.fetchone():
        cur.close()
        return False, 'Este usuario ya está registrado como empleado'
    
    cur.close()
    return True, None

@jwt_required()
def cntlistado_empleados():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except (TypeError, ValueError):
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser números enteros'}), 400

    if page <= 0 or per_page <= 0:
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser mayores que cero'}), 400

    service = EmpleadoService(current_app.mysql)
    return jsonify(service.listar_todos(page, per_page))

@jwt_required()
def cntobtener_empleado(id_empleado):
    service = EmpleadoService(current_app.mysql)
    empleado = service.obtener_por_id(id_empleado)
    if empleado:
        return jsonify(empleado)
    return jsonify({'error': 'Empleado no encontrado'}), 404

@jwt_required()
def cntcrear_empleado():
    data = request.get_json()
    es_valido, mensaje = validar_datos_empleado(data)
    if not es_valido:
        return jsonify({'error': mensaje}), 400

    service = EmpleadoService(current_app.mysql)
    empleado = service.crear(
        id_usuario=data.get('id_usuario'),
        nombre=data.get('nombre'),
        apellido=data.get('apellido'),
        telefono=data.get('telefono'),
        cargo=data.get('cargo'),
        especialidad=data.get('especialidad')
    )
    return jsonify(empleado), 201
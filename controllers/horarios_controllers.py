from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required
from services.horarios_services import HorarioService

def validar_datos_horario(data):
    # ← Esta función NO lleva @jwt_required() porque no es un endpoint
    id_empleado = data.get('id_empleado')
    dia = data.get('dia_semana')
    h_inicio = data.get('hora_inicio')
    h_fin = data.get('hora_fin')
    if not id_empleado or not dia or not h_inicio or not h_fin:
        return False, 'Todos los campos (empleado, día, inicio y fin) son necesarios'
    
    cur = current_app.mysql.connection.cursor()
    cur.execute("SELECT * FROM empleados WHERE emp_id = %s", (id_empleado,))
    if not cur.fetchone():
        cur.close()
        return False, 'El empleado indicado no existe'
    cur.execute("SELECT * FROM horarios WHERE hor_empleado_id = %s AND hor_dia_semana = %s", (id_empleado, dia))
    if cur.fetchone():
        cur.close()
        return False, f'El empleado ya tiene un horario registrado para el día {dia}'
    
    cur.close()
    return True, None

@jwt_required()
def cntlistado_horarios():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except (TypeError, ValueError):
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser números enteros'}), 400

    if page <= 0 or per_page <= 0:
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser mayores que cero'}), 400

    service = HorarioService(current_app.mysql)
    return jsonify(service.listar_todos(page, per_page))

@jwt_required()
def cntlistado_por_empleado(id_empleado):
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except (TypeError, ValueError):
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser números enteros'}), 400

    if page <= 0 or per_page <= 0:
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser mayores que cero'}), 400

    service = HorarioService(current_app.mysql)
    return jsonify(service.listar_por_empleado(id_empleado, page, per_page))

@jwt_required()
def cntcrear_horario():
    data = request.get_json()
    es_valido, mensaje = validar_datos_horario(data)
    if not es_valido:
        return jsonify({'error': mensaje}), 400
    service = HorarioService(current_app.mysql)
    horario = service.crear(
        id_empleado=data.get('id_empleado'),
        dia_semana=data.get('dia_semana'),
        hora_inicio=data.get('hora_inicio'),
        hora_fin=data.get('hora_fin')
    )
    return jsonify(horario), 201
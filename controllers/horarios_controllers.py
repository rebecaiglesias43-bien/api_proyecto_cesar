from flask import request, jsonify, current_app
from services.horarios_services import HorarioService
def validar_datos_horario(data):
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
def cntlistado_horarios():
    service = HorarioService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntlistado_por_empleado(id_empleado):
    service = HorarioService(current_app.mysql)
    return jsonify(service.listar_por_empleado(id_empleado))

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
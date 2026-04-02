from flask import request, jsonify, current_app
from services.horario_services import HorarioService

def cntlistado_horarios():
    service = HorarioService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntlistado_por_empleado(id_empleado):
    service = HorarioService(current_app.mysql)
    return jsonify(service.listar_por_empleado(id_empleado))

def cntcrear_horario():
    data = request.get_json()
    service = HorarioService(current_app.mysql)
    horario = service.crear(
        id_empleado=data.get('id_empleado'),
        dia_semana=data.get('dia_semana'),
        hora_inicio=data.get('hora_inicio'),
        hora_fin=data.get('hora_fin')
    )
    return jsonify(horario), 201
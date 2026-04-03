from flask import request, jsonify, current_app
from services.cita_services import CitaService

def cntlistado_citas():
    service = CitaService(current_app.mysql)
    return jsonify(service.listar_todas())

def cntobtener_cita(id_cita):
    service = CitaService(current_app.mysql)
    cita = service.obtener_por_id(id_cita)
    if cita:
        return jsonify(cita)
    return jsonify({'error': 'Cita no encontrada'}), 404

def cntcrear_cita():
    data = request.get_json()
    service = CitaService(current_app.mysql)
    cita = service.crear(
        id_cliente=data.get('id_cliente'),
        id_empleado=data.get('id_empleado'),
        fecha=data.get('fecha'),
        hora=data.get('hora'),
        estado=data.get('estado')
    )
    return jsonify(cita), 201
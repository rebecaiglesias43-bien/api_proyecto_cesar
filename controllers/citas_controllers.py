from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required
from services.citas_services import CitaService

def cntlistado_citas():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except (TypeError, ValueError):
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser números enteros'}), 400
    
    if page <= 0 or per_page <= 0:
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser mayores que cero'}), 400
    
    service = CitaService(current_app.mysql)
    return jsonify(service.listar_todas(page, per_page))



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

def cntactualizar_cita(id_cita):
    data = request.get_json()
    service = CitaService(current_app.mysql)
    cita = service.actualizar(
        id_cita=id_cita,
        id_cliente=data.get('id_cliente'),
        id_empleado=data.get('id_empleado'),
        fecha=data.get('fecha'),
        hora=data.get('hora'),
        estado=data.get('estado')
    )
    if cita:
        return jsonify(cita)
    return jsonify({'error': 'Cita no encontrada'}), 404

def cnteliminar_cita(id_cita):
    service = CitaService(current_app.mysql)
    eliminado = service.eliminar(id_cita)
    if eliminado:
        return jsonify({'mensaje': 'Cita eliminada correctamente'})
    return jsonify({'error': 'Cita no encontrada'}), 404

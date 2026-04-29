from flask import request, jsonify, current_app
from services.detalles_citas_services import DetalleCitaService

from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required
from services.detalles_citas_services import DetalleCitaService

def cntlistado_detalles():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except (TypeError, ValueError):
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser números enteros'}), 400
    
    if page <= 0 or per_page <= 0:
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser mayores que cero'}), 400
    
    service = DetalleCitaService(current_app.mysql)
    return jsonify(service.listar_todos(page, per_page))



def cntlistado_detalles_por_cita(id_cita):
    service = DetalleCitaService(current_app.mysql)
    return jsonify(service.listar_por_cita(id_cita))

def cntcrear_detalle():
    data = request.get_json()
    service = DetalleCitaService(current_app.mysql)
    detalle = service.crear(
        id_cita=data.get('id_cita'),
        id_servicio=data.get('id_servicio'),
        precio=data.get('precio')
    )
    return jsonify(detalle), 201

def cntactualizar_detalle(id_detalle):
    data = request.get_json()
    service = DetalleCitaService(current_app.mysql)
    detalle = service.actualizar(
        id_detalle=id_detalle,
        id_cita=data.get('id_cita'),
        id_servicio=data.get('id_servicio'),
        precio=data.get('precio')
    )
    if detalle:
        return jsonify(detalle)
    return jsonify({'error': 'Detalle de cita no encontrado'}), 404

def cnteliminar_detalle(id_detalle):
    service = DetalleCitaService(current_app.mysql)
    eliminado = service.eliminar(id_detalle)
    if eliminado:
        return jsonify({'mensaje': 'Detalle de cita eliminado correctamente'})
    return jsonify({'error': 'Detalle de cita no encontrado'}), 404

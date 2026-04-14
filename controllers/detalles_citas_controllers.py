from flask import request, jsonify, current_app
from services.detalles_citas_services import DetalleCitaService

def cntlistado_detalles():
    service = DetalleCitaService(current_app.mysql)
    return jsonify(service.listar_todos())

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
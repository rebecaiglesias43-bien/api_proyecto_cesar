from flask import request, jsonify, current_app
from services.facturas_services import FacturaService

def cntlistado_facturas():
    service = FacturaService(current_app.mysql)
    return jsonify(service.listar_todas())

def cntobtener_factura(id_factura):
    service = FacturaService(current_app.mysql)
    factura = service.obtener_por_id(id_factura)
    if factura:
        return jsonify(factura)
    return jsonify({'error': 'Factura no encontrada'}), 404

def cntobtener_factura_por_cita(id_cita):
    service = FacturaService(current_app.mysql)
    factura = service.obtener_por_cita(id_cita)
    if factura:
        return jsonify(factura)
    return jsonify({'error': 'Factura no encontrada para esta cita'}), 404

def cntcrear_factura():
    data = request.get_json()
    service = FacturaService(current_app.mysql)
    factura = service.crear(
        id_cita=data.get('id_cita'),
        total=data.get('total'),
        estado=data.get('estado', 'pendiente')
    )
    return jsonify(factura), 201

def cntactualizar_estado_factura(id_factura):
    data = request.get_json()
    service = FacturaService(current_app.mysql)
    factura = service.actualizar_estado(id_factura, data.get('estado'))
    if factura:
        return jsonify(factura)
    return jsonify({'error': 'Factura no encontrada'}), 404
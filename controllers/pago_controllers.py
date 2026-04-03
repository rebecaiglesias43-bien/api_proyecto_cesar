from flask import request, jsonify, current_app
from services.pago_services import PagoService

def cntlistado_pagos():
    service = PagoService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntobtener_pago(id_pago):
    service = PagoService(current_app.mysql)
    pago = service.obtener_por_id(id_pago)
    if pago:
        return jsonify(pago)
    return jsonify({'error': 'Pago no encontrado'}), 404

def cntlistado_por_factura(id_factura):
    service = PagoService(current_app.mysql)
    return jsonify(service.listar_por_factura(id_factura))

def cntcrear_pago():
    data = request.get_json()
    service = PagoService(current_app.mysql)
    pago = service.crear(
        id_factura=data.get('id_factura'),
        metodo=data.get('metodo'),
        monto=data.get('monto')
    )
    return jsonify(pago), 201
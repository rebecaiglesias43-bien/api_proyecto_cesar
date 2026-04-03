from flask import request, jsonify, current_app
from services.detalle_factura_services import DetalleFacturaService

def cntlistado_detalles_factura():
    service = DetalleFacturaService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntlistado_por_factura(id_factura):
    service = DetalleFacturaService(current_app.mysql)
    return jsonify(service.listar_por_factura(id_factura))

def cntcrear_detalle_factura():
    data = request.get_json()
    service = DetalleFacturaService(current_app.mysql)
    detalle = service.crear(
        id_factura=data.get('id_factura'),
        id_servicio=data.get('id_servicio'),
        subtotal=data.get('subtotal')
    )
    return jsonify(detalle), 201
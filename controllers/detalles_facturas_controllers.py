from flask import request, jsonify, current_app
from services.detalles_facturas_services import DetalleFacturaService


def _get_json_body():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return None, (jsonify({'error': 'El cuerpo de la solicitud debe ser un objeto JSON'}), 400)
    return data, None


def _is_positive_int(value):
    try:
        return isinstance(value, bool) is False and int(value) > 0
    except Exception:
        return False


def _is_non_negative_number(value):
    try:
        return float(value) >= 0
    except Exception:
        return False


def cntlistado_detalles_factura():
    service = DetalleFacturaService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntlistado_por_factura(id_factura):
    service = DetalleFacturaService(current_app.mysql)
    return jsonify(service.listar_por_factura(id_factura))

def cntcrear_detalle_factura():
    data, error = _get_json_body()
    if error:
        return error

    id_factura = data.get('id_factura')
    id_servicio = data.get('id_servicio')
    subtotal = data.get('subtotal')

    if not _is_positive_int(id_factura):
        return jsonify({'error': 'id_factura es requerido y debe ser un entero positivo'}), 400
    if not _is_positive_int(id_servicio):
        return jsonify({'error': 'id_servicio es requerido y debe ser un entero positivo'}), 400
    if subtotal is None or not _is_non_negative_number(subtotal):
        return jsonify({'error': 'subtotal es requerido y debe ser un número no negativo'}), 400

    service = DetalleFacturaService(current_app.mysql)
    detalle = service.crear(
        id_factura=int(id_factura),
        id_servicio=int(id_servicio),
        subtotal=float(subtotal)
    )
    return jsonify(detalle), 201
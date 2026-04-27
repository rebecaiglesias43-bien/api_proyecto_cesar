from flask import request, jsonify, current_app
from services.pagos_services import PagoService


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


def _is_non_empty_string(value):
    return isinstance(value, str) and value.strip() != ''


def _is_non_negative_number(value):
    try:
        return float(value) >= 0
    except Exception:
        return False


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
    data, error = _get_json_body()
    if error:
        return error

    id_factura = data.get('id_factura')
    metodo = data.get('metodo')
    monto = data.get('monto')

    if not _is_positive_int(id_factura):
        return jsonify({'error': 'id_factura es requerido y debe ser un entero positivo'}), 400
    if not _is_non_empty_string(metodo):
        return jsonify({'error': 'metodo es requerido y debe ser texto'}), 400
    if monto is None or not _is_non_negative_number(monto):
        return jsonify({'error': 'monto es requerido y debe ser un número no negativo'}), 400

    service = PagoService(current_app.mysql)
    pago = service.crear(
        id_factura=int(id_factura),
        metodo=metodo.strip(),
        monto=float(monto)
    )
    return jsonify(pago), 201
from flask import request, jsonify, current_app
from services.facturas_services import FacturaService

VALID_ESTADOS = {'pendiente', 'pagado', 'cancelado'}


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
    data, error = _get_json_body()
    if error:
        return error

    id_cita = data.get('id_cita')
    total = data.get('total')
    estado = data.get('estado', 'pendiente')

    if not _is_positive_int(id_cita):
        return jsonify({'error': 'id_cita es requerido y debe ser un entero positivo'}), 400
    if total is None or not _is_non_negative_number(total):
        return jsonify({'error': 'total es requerido y debe ser un número no negativo'}), 400
    if estado not in VALID_ESTADOS:
        return jsonify({'error': f'estado inválido. Valores permitidos: {", ".join(VALID_ESTADOS)}'}), 400

    service = FacturaService(current_app.mysql)
    factura = service.crear(
        id_cita=int(id_cita),
        total=float(total),
        estado=estado
    )
    return jsonify(factura), 201

def cntactualizar_estado_factura(id_factura):
    data, error = _get_json_body()
    if error:
        return error

    estado = data.get('estado')
    if estado not in VALID_ESTADOS:
        return jsonify({'error': f'estado inválido. Valores permitidos: {", ".join(VALID_ESTADOS)}'}), 400

    service = FacturaService(current_app.mysql)
    factura = service.actualizar_estado(id_factura, estado)
    if factura:
        return jsonify(factura)
    return jsonify({'error': 'Factura no encontrada'}), 404
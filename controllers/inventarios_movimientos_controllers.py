from datetime import datetime

from flask import request, jsonify, current_app
from services.inventarios_movimientos_services import InventarioMovimientoService


TIPOS_PERMITIDOS = {'entrada', 'salida'}


def _validar_entero_positivo(data, campo):
    valor = data.get(campo)
    if valor is None:
        return None, f'El campo "{campo}" es requerido'
    if isinstance(valor, bool) or not isinstance(valor, int):
        return None, f'El campo "{campo}" debe ser un numero entero'
    if valor <= 0:
        return None, f'El campo "{campo}" debe ser mayor que cero'
    return valor, None


def _validar_payload(data):
    if not isinstance(data, dict):
        return None, ('El cuerpo de la solicitud debe ser un objeto JSON', 400)

    id_producto, error = _validar_entero_positivo(data, 'id_producto')
    if error:
        return None, (error, 400)

    tipo = data.get('tipo')
    if not isinstance(tipo, str) or not tipo.strip():
        return None, ('El campo "tipo" es requerido y debe ser texto', 400)
    tipo = tipo.strip().lower()
    if tipo not in TIPOS_PERMITIDOS:
        return None, ('El campo "tipo" debe ser "entrada" o "salida"', 400)

    cantidad, error = _validar_entero_positivo(data, 'cantidad')
    if error:
        return None, (error, 400)

    fecha = data.get('fecha')
    if not isinstance(fecha, str) or not fecha.strip():
        return None, ('El campo "fecha" es requerido y debe tener formato YYYY-MM-DD', 400)
    try:
        fecha = datetime.strptime(fecha.strip(), '%Y-%m-%d').date().isoformat()
    except ValueError:
        return None, ('El campo "fecha" debe tener formato YYYY-MM-DD', 400)

    motivo = data.get('motivo')
    if motivo is not None:
        if not isinstance(motivo, str):
            return None, ('El campo "motivo" debe ser una cadena de texto', 400)
        motivo = motivo.strip() or None
        if motivo and len(motivo) > 50:
            return None, ('El campo "motivo" supera el maximo de 50 caracteres', 400)

    return {
        'id_producto': id_producto,
        'tipo': tipo,
        'cantidad': cantidad,
        'fecha': fecha,
        'motivo': motivo
    }, None


def cntlistado_inventario_movimientos():
    service = InventarioMovimientoService(current_app.mysql)
    return jsonify(service.listar_todos())


def cntobtener_inventario_movimiento(id_movimiento):
    service = InventarioMovimientoService(current_app.mysql)
    movimiento = service.obtener_por_id(id_movimiento)
    if movimiento:
        return jsonify(movimiento)
    return jsonify({'error': 'Movimiento de inventario no encontrado'}), 404


def cntcrear_inventario_movimiento():
    data = request.get_json(silent=True) or {}
    payload, error = _validar_payload(data)
    if error:
        return jsonify({'error': error[0]}), error[1]

    service = InventarioMovimientoService(current_app.mysql)
    try:
        movimiento = service.crear(
            id_producto=payload['id_producto'],
            tipo=payload['tipo'],
            cantidad=payload['cantidad'],
            fecha=payload['fecha'],
            motivo=payload['motivo']
        )
    except LookupError as exc:
        return jsonify({'error': str(exc)}), 404
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    return jsonify(movimiento), 201


def cntactualizar_inventario_movimiento(id_movimiento):
    data = request.get_json(silent=True) or {}
    payload, error = _validar_payload(data)
    if error:
        return jsonify({'error': error[0]}), error[1]

    service = InventarioMovimientoService(current_app.mysql)
    try:
        movimiento = service.actualizar(
            id_movimiento=id_movimiento,
            id_producto=payload['id_producto'],
            tipo=payload['tipo'],
            cantidad=payload['cantidad'],
            fecha=payload['fecha'],
            motivo=payload['motivo']
        )
    except LookupError as exc:
        return jsonify({'error': str(exc)}), 404
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    if movimiento:
        return jsonify(movimiento)
    return jsonify({'error': 'Movimiento de inventario no encontrado'}), 404


def cnteliminar_inventario_movimiento(id_movimiento):
    service = InventarioMovimientoService(current_app.mysql)
    if service.eliminar(id_movimiento):
        return jsonify({'mensaje': 'Movimiento de inventario eliminado correctamente'})
    return jsonify({'error': 'Movimiento de inventario no encontrado'}), 404

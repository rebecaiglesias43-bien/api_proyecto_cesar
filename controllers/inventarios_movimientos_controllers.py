from flask import request, jsonify, current_app
from services.inventarios_movimientos_services import InventarioMovimientoService


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
    id_producto = data.get('id_producto')
    tipo = data.get('tipo')
    cantidad = data.get('cantidad')
    fecha = data.get('fecha')

    if id_producto is None or not tipo or cantidad is None or not fecha:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    service = InventarioMovimientoService(current_app.mysql)
    movimiento = service.crear(
        id_producto=id_producto,
        tipo=tipo,
        cantidad=cantidad,
        fecha=fecha,
        motivo=data.get('motivo')
    )
    return jsonify(movimiento), 201


def cntactualizar_inventario_movimiento(id_movimiento):
    data = request.get_json(silent=True) or {}
    id_producto = data.get('id_producto')
    tipo = data.get('tipo')
    cantidad = data.get('cantidad')
    fecha = data.get('fecha')

    if id_producto is None or not tipo or cantidad is None or not fecha:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    service = InventarioMovimientoService(current_app.mysql)
    movimiento = service.actualizar(
        id_movimiento=id_movimiento,
        id_producto=id_producto,
        tipo=tipo,
        cantidad=cantidad,
        fecha=fecha,
        motivo=data.get('motivo')
    )
    if movimiento:
        return jsonify(movimiento)
    return jsonify({'error': 'Movimiento de inventario no encontrado'}), 404


def cnteliminar_inventario_movimiento(id_movimiento):
    service = InventarioMovimientoService(current_app.mysql)
    if service.eliminar(id_movimiento):
        return jsonify({'mensaje': 'Movimiento de inventario eliminado correctamente'})
    return jsonify({'error': 'Movimiento de inventario no encontrado'}), 404

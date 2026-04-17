from flask import request, jsonify, current_app
from services.proveedores_productos_services import ProveedorProductoService


def cntlistado_proveedores_productos():
    service = ProveedorProductoService(current_app.mysql)
    return jsonify(service.listar_todos())


def cntobtener_proveedor_producto(id_relacion):
    service = ProveedorProductoService(current_app.mysql)
    relacion = service.obtener_por_id(id_relacion)
    if relacion:
        return jsonify(relacion)
    return jsonify({'error': 'Relacion proveedor-producto no encontrada'}), 404


def cntcrear_proveedor_producto():
    data = request.get_json(silent=True) or {}
    id_proveedor = data.get('id_proveedor')
    id_producto = data.get('id_producto')
    precio = data.get('precio')

    if id_proveedor is None or id_producto is None or precio is None:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    service = ProveedorProductoService(current_app.mysql)
    relacion = service.crear(id_proveedor, id_producto, precio)
    return jsonify(relacion), 201


def cntactualizar_proveedor_producto(id_relacion):
    data = request.get_json(silent=True) or {}
    id_proveedor = data.get('id_proveedor')
    id_producto = data.get('id_producto')
    precio = data.get('precio')

    if id_proveedor is None or id_producto is None or precio is None:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    service = ProveedorProductoService(current_app.mysql)
    relacion = service.actualizar(id_relacion, id_proveedor, id_producto, precio)
    if relacion:
        return jsonify(relacion)
    return jsonify({'error': 'Relacion proveedor-producto no encontrada'}), 404


def cnteliminar_proveedor_producto(id_relacion):
    service = ProveedorProductoService(current_app.mysql)
    if service.eliminar(id_relacion):
        return jsonify({'mensaje': 'Relacion proveedor-producto eliminada correctamente'})
    return jsonify({'error': 'Relacion proveedor-producto no encontrada'}), 404

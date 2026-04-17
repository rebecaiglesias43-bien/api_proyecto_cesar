from flask import request, jsonify, current_app
from services.proveedores_services import ProveedorService


def cntlistado_proveedores():
    service = ProveedorService(current_app.mysql)
    return jsonify(service.listar_todos())


def cntobtener_proveedor(id_proveedor):
    service = ProveedorService(current_app.mysql)
    proveedor = service.obtener_por_id(id_proveedor)
    if proveedor:
        return jsonify(proveedor)
    return jsonify({'error': 'Proveedor no encontrado'}), 404


def cntcrear_proveedor():
    data = request.get_json(silent=True) or {}
    nombre = data.get('nombre')

    if not nombre:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    service = ProveedorService(current_app.mysql)
    proveedor = service.crear(
        nombre=nombre,
        telefono=data.get('telefono'),
        email=data.get('email'),
        direccion=data.get('direccion')
    )
    return jsonify(proveedor), 201


def cntactualizar_proveedor(id_proveedor):
    data = request.get_json(silent=True) or {}
    nombre = data.get('nombre')

    if not nombre:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    service = ProveedorService(current_app.mysql)
    proveedor = service.actualizar(
        id_proveedor=id_proveedor,
        nombre=nombre,
        telefono=data.get('telefono'),
        email=data.get('email'),
        direccion=data.get('direccion')
    )
    if proveedor:
        return jsonify(proveedor)
    return jsonify({'error': 'Proveedor no encontrado'}), 404


def cnteliminar_proveedor(id_proveedor):
    service = ProveedorService(current_app.mysql)
    if service.eliminar(id_proveedor):
        return jsonify({'mensaje': 'Proveedor eliminado'})
    return jsonify({'error': 'Proveedor no encontrado'}), 404

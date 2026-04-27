from decimal import Decimal, InvalidOperation

from flask import request, jsonify, current_app
from services.proveedores_productos_services import ProveedorProductoService


def _validar_entero_positivo(data, campo):
    valor = data.get(campo)
    if valor is None:
        return None, f'El campo "{campo}" es requerido'
    if isinstance(valor, bool) or not isinstance(valor, int):
        return None, f'El campo "{campo}" debe ser un numero entero'
    if valor <= 0:
        return None, f'El campo "{campo}" debe ser mayor que cero'
    return valor, None


def _validar_precio(data):
    valor = data.get('precio')
    if valor is None:
        return None, 'El campo "precio" es requerido'

    try:
        precio = Decimal(str(valor))
    except (InvalidOperation, TypeError, ValueError):
        return None, 'El campo "precio" debe ser un numero valido'

    if precio < 0:
        return None, 'El campo "precio" no puede ser negativo'

    return precio, None


def _validar_payload(data):
    if not isinstance(data, dict):
        return None, ('El cuerpo de la solicitud debe ser un objeto JSON', 400)

    id_proveedor, error = _validar_entero_positivo(data, 'id_proveedor')
    if error:
        return None, (error, 400)

    id_producto, error = _validar_entero_positivo(data, 'id_producto')
    if error:
        return None, (error, 400)

    precio, error = _validar_precio(data)
    if error:
        return None, (error, 400)

    return {
        'id_proveedor': id_proveedor,
        'id_producto': id_producto,
        'precio': precio
    }, None


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
    payload, error = _validar_payload(data)
    if error:
        return jsonify({'error': error[0]}), error[1]

    service = ProveedorProductoService(current_app.mysql)
    try:
        relacion = service.crear(
            payload['id_proveedor'],
            payload['id_producto'],
            payload['precio']
        )
    except LookupError as exc:
        return jsonify({'error': str(exc)}), 404
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    return jsonify(relacion), 201


def cntactualizar_proveedor_producto(id_relacion):
    data = request.get_json(silent=True) or {}
    payload, error = _validar_payload(data)
    if error:
        return jsonify({'error': error[0]}), error[1]

    service = ProveedorProductoService(current_app.mysql)
    try:
        relacion = service.actualizar(
            id_relacion,
            payload['id_proveedor'],
            payload['id_producto'],
            payload['precio']
        )
    except LookupError as exc:
        return jsonify({'error': str(exc)}), 404
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    if relacion:
        return jsonify(relacion)
    return jsonify({'error': 'Relacion proveedor-producto no encontrada'}), 404


def cnteliminar_proveedor_producto(id_relacion):
    service = ProveedorProductoService(current_app.mysql)
    if service.eliminar(id_relacion):
        return jsonify({'mensaje': 'Relacion proveedor-producto eliminada correctamente'})
    return jsonify({'error': 'Relacion proveedor-producto no encontrada'}), 404

from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required
from services.servicios_productos_services import ServicioProductoService

def cntlistado_servicios_productos():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except (TypeError, ValueError):
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser números enteros'}), 400
    
    if page <= 0 or per_page <= 0:
        return jsonify({'error': 'Los parámetros "page" y "per_page" deben ser mayores que cero'}), 400
    
    service = ServicioProductoService(current_app.mysql)
    return jsonify(service.listar_todos(page, per_page))

def cntcrear_servicio_producto():
    data = request.get_json()
    id_servicio = data.get('id_servicio')
    id_producto = data.get('id_producto')
    cantidad = data.get('cantidad')

    if not all([id_servicio, id_producto, cantidad]):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    service = ServicioProductoService(current_app.mysql)
    relacion = service.crear(id_servicio, id_producto, cantidad)
    return jsonify(relacion), 201

def cntactualizar_servicio_producto(id_relacion):
    data = request.get_json()
    service = ServicioProductoService(current_app.mysql)
    relacion = service.actualizar(
        id_relacion=id_relacion,
        id_servicio=data.get('id_servicio'),
        id_producto=data.get('id_producto'),
        cantidad=data.get('cantidad')
    )
    if relacion:
        return jsonify(relacion)
    return jsonify({'error': 'Relación servicio-producto no encontrada'}), 404

def cnteliminar_servicio_producto(id_relacion):
    service = ServicioProductoService(current_app.mysql)
    eliminado = service.eliminar(id_relacion)
    if eliminado:
        return jsonify({'mensaje': 'Relación servicio-producto eliminada correctamente'})
    return jsonify({'error': 'Relación servicio-producto no encontrada'}), 404
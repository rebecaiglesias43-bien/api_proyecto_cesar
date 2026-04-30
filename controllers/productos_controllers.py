from flask import request, jsonify, current_app
from services.productos_services import ProductoService


def _obtener_paginacion():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except (TypeError, ValueError):
        return None, jsonify({'error': 'Los parametros "page" y "per_page" deben ser numeros enteros'}), 400
    if page <= 0 or per_page <= 0:
        return None, jsonify({'error': 'Los parametros "page" y "per_page" deben ser mayores que cero'}), 400
    return {'page': page, 'per_page': per_page}, None, None


def cntlistado_productos():
    paginacion, response, status = _obtener_paginacion()
    if response is not None:
        return response, status
    service = ProductoService(current_app.mysql)
    return jsonify(service.listar_todos(paginacion['page'], paginacion['per_page']))

def cntobtener_producto(id_producto):
    service = ProductoService(current_app.mysql)
    producto = service.obtener_por_id(id_producto)
    if producto:
        return jsonify(producto)
    return jsonify({'error': 'Producto no encontrado'}), 404

def cntcrear_producto():
    data = request.get_json(silent=True)
    service = ProductoService(current_app.mysql)
    try:
        producto = service.crear(data)
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    return jsonify(producto), 201

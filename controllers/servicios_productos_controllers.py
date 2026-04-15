from flask import request, jsonify, current_app
from services.servicios_productos_services import ServicioProductoService

def cntlistado_servicios_productos():
    service = ServicioProductoService(current_app.mysql)
    return jsonify(service.listar_todos())

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

from flask import jsonify, current_app
from services.servicio_producto_services import ServicioProductoService

def cntlistado_servicios_productos():
    service = ServicioProductoService(current_app.mysql)
    return jsonify(service.listar_todos())
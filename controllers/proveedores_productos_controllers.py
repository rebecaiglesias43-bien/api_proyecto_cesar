from flask import jsonify, current_app
from services.proveedores_productos_services import ProveedorProductoService

def cntlistado_proveedores_productos():
    service = ProveedorProductoService(current_app.mysql)
    return jsonify(service.listar_todos())


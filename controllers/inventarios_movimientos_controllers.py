from flask import jsonify, current_app
from services.inventarios_movimientos_services import InventarioMovimientoService

def cntlistado_inventario_movimientos():
    service = InventarioMovimientoService(current_app.mysql)
    return jsonify(service.listar_todos())
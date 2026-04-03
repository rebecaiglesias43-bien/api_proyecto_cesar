from flask import Blueprint
from controllers.inventario_movimiento_controllers import cntlistado_inventario_movimientos

inventario_movimiento_bp = Blueprint('inventario_movimientos', __name__)

@inventario_movimiento_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_inventario_movimientos()
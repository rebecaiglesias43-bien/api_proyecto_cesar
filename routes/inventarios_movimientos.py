from flask import Blueprint
from controllers.inventarios_movimientos_controllers import (
    cntlistado_inventario_movimientos,
    cntobtener_inventario_movimiento,
    cntcrear_inventario_movimiento,
    cntactualizar_inventario_movimiento,
    cnteliminar_inventario_movimiento
)

inventario_movimiento_bp = Blueprint('inventario_movimientos', __name__)


@inventario_movimiento_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_inventario_movimientos()


@inventario_movimiento_bp.route('/<int:id_movimiento>', methods=['GET'])
def obtener(id_movimiento):
    return cntobtener_inventario_movimiento(id_movimiento)


@inventario_movimiento_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_inventario_movimiento()


@inventario_movimiento_bp.route('/<int:id_movimiento>', methods=['PUT'])
def actualizar(id_movimiento):
    return cntactualizar_inventario_movimiento(id_movimiento)


@inventario_movimiento_bp.route('/<int:id_movimiento>', methods=['DELETE'])
def eliminar(id_movimiento):
    return cnteliminar_inventario_movimiento(id_movimiento)

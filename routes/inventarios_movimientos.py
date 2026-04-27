from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers.inventarios_movimientos_controllers import (
    cntactualizar_inventario_movimiento,
    cntcrear_inventario_movimiento,
    cnteliminar_inventario_movimiento,
    cntlistado_inventario_movimientos,
    cntobtener_inventario_movimiento,
)

inventario_movimiento_bp = Blueprint('inventario_movimientos', __name__)


@inventario_movimiento_bp.route('/', methods=['GET'])
@jwt_required()
def listado():
    return cntlistado_inventario_movimientos()


@inventario_movimiento_bp.route('/<int:id_movimiento>', methods=['GET'])
@jwt_required()
def obtener(id_movimiento):
    return cntobtener_inventario_movimiento(id_movimiento)


@inventario_movimiento_bp.route('/', methods=['POST'])
@jwt_required()
def crear():
    return cntcrear_inventario_movimiento()


@inventario_movimiento_bp.route('/<int:id_movimiento>', methods=['PUT'])
@jwt_required()
def actualizar(id_movimiento):
    return cntactualizar_inventario_movimiento(id_movimiento)


@inventario_movimiento_bp.route('/<int:id_movimiento>', methods=['DELETE'])
@jwt_required()
def eliminar(id_movimiento):
    return cnteliminar_inventario_movimiento(id_movimiento)

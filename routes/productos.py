from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers.productos_controllers import (
    cntcrear_producto,
    cntlistado_productos,
    cntobtener_producto,
)

producto_bp = Blueprint('productos', __name__)


@producto_bp.route('/', methods=['GET'])
@jwt_required()
def listado():
    return cntlistado_productos()


@producto_bp.route('/<int:id_producto>', methods=['GET'])
@jwt_required()
def obtener(id_producto):
    return cntobtener_producto(id_producto)


@producto_bp.route('/', methods=['POST'])
@jwt_required()
def crear():
    return cntcrear_producto()

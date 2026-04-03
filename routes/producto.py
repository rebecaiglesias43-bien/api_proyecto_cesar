from flask import Blueprint
from controllers.producto_controllers import (
    cntlistado_productos, cntobtener_producto, cntcrear_producto
)

producto_bp = Blueprint('productos', __name__)

@producto_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_productos()

@producto_bp.route('/<int:id_producto>', methods=['GET'])
def obtener(id_producto):
    return cntobtener_producto(id_producto)

@producto_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_producto()
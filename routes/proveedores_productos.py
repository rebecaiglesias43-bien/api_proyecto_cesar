from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers.proveedores_productos_controllers import (
    cntactualizar_proveedor_producto,
    cntcrear_proveedor_producto,
    cnteliminar_proveedor_producto,
    cntlistado_proveedores_productos,
    cntobtener_proveedor_producto,
)

proveedor_producto_bp = Blueprint('proveedores_productos', __name__)


@proveedor_producto_bp.route('/', methods=['GET'])
@jwt_required()
def listado():
    return cntlistado_proveedores_productos()


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['GET'])
@jwt_required()
def obtener(id_relacion):
    return cntobtener_proveedor_producto(id_relacion)


@proveedor_producto_bp.route('/', methods=['POST'])
@jwt_required()
def crear():
    return cntcrear_proveedor_producto()


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['PUT'])
@jwt_required()
def actualizar(id_relacion):
    return cntactualizar_proveedor_producto(id_relacion)


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['DELETE'])
@jwt_required()
def eliminar(id_relacion):
    return cnteliminar_proveedor_producto(id_relacion)

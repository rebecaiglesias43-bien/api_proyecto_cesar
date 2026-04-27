from flask import Blueprint
from controllers.proveedores_productos_controllers import (
    cntlistado_proveedores_productos,
    cntobtener_proveedor_producto,
    cntcrear_proveedor_producto,
    cntactualizar_proveedor_producto,
    cnteliminar_proveedor_producto
)

proveedor_producto_bp = Blueprint('proveedores_productos', __name__)


@proveedor_producto_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_proveedores_productos()


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['GET'])
def obtener(id_relacion):
    return cntobtener_proveedor_producto(id_relacion)


@proveedor_producto_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_proveedor_producto()


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['PUT'])
def actualizar(id_relacion):
    return cntactualizar_proveedor_producto(id_relacion)


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['DELETE'])
def eliminar(id_relacion):
    return cnteliminar_proveedor_producto(id_relacion)

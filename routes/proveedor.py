from flask import Blueprint
from controllers.proveedor_controllers import (
    cntlistado_proveedores, cntobtener_proveedor,
    cntcrear_proveedor, cntactualizar_proveedor, cnteliminar_proveedor
)

proveedor_bp = Blueprint('proveedor', __name__)

@proveedor_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_proveedores()

@proveedor_bp.route('/<int:id_proveedor>', methods=['GET'])
def obtener(id_proveedor):
    return cntobtener_proveedor(id_proveedor)

@proveedor_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_proveedor()

@proveedor_bp.route('/<int:id_proveedor>', methods=['PUT'])
def actualizar(id_proveedor):
    return cntactualizar_proveedor(id_proveedor)

@proveedor_bp.route('/<int:id_proveedor>', methods=['DELETE'])
def eliminar(id_proveedor):
    return cnteliminar_proveedor(id_proveedor)
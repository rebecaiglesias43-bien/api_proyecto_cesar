from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers.proveedores_controllers import (
    cntactualizar_proveedor,
    cntcrear_proveedor,
    cnteliminar_proveedor,
    cntlistado_proveedores,
    cntobtener_proveedor,
)

proveedor_bp = Blueprint('proveedor', __name__)


@proveedor_bp.route('/', methods=['GET'])
@jwt_required()
def listado():
    return cntlistado_proveedores()


@proveedor_bp.route('/<int:id_proveedor>', methods=['GET'])
@jwt_required()
def obtener(id_proveedor):
    return cntobtener_proveedor(id_proveedor)


@proveedor_bp.route('/', methods=['POST'])
@jwt_required()
def crear():
    return cntcrear_proveedor()


@proveedor_bp.route('/<int:id_proveedor>', methods=['PUT'])
@jwt_required()
def actualizar(id_proveedor):
    return cntactualizar_proveedor(id_proveedor)


@proveedor_bp.route('/<int:id_proveedor>', methods=['DELETE'])
@jwt_required()
def eliminar(id_proveedor):
    return cnteliminar_proveedor(id_proveedor)

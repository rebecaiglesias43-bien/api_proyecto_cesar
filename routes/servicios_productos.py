from flask import Blueprint
from controllers.servicios_productos_controllers import (
    cntlistado_servicios_productos,
    cntactualizar_servicio_producto,
    cnteliminar_servicio_producto,
    cntcrear_servicio_producto
)

servicio_producto_bp = Blueprint('servicios_productos', __name__)

@servicio_producto_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_servicios_productos()

@servicio_producto_bp.route('/crear', methods=['POST'])
def crear():
    return cntcrear_servicio_producto()

@servicio_producto_bp.route('/<int:id_relacion>', methods=['PUT'])
def actualizar(id_relacion):
    return cntactualizar_servicio_producto(id_relacion)

@servicio_producto_bp.route('/<int:id_relacion>', methods=['DELETE'])
def eliminar(id_relacion):
    return cnteliminar_servicio_producto(id_relacion)
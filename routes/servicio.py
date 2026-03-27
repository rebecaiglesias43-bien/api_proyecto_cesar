from flask import Blueprint
from controllers.servicio_controllers import (
    cntlistado_servicios, cntobtener_servicio, cntcrear_servicio,
    cntactualizar_servicio, cnteliminar_servicio
)

servicio_bp = Blueprint('servicio', __name__)

@servicio_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_servicios()

@servicio_bp.route('/<int:id_servicio>', methods=['GET'])
def obtener(id_servicio):
    return cntobtener_servicio(id_servicio)

@servicio_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_servicio()

@servicio_bp.route('/<int:id_servicio>', methods=['PUT'])
def actualizar(id_servicio):
    return cntactualizar_servicio(id_servicio)

@servicio_bp.route('/<int:id_servicio>', methods=['DELETE'])
def eliminar(id_servicio):
    return cnteliminar_servicio(id_servicio)

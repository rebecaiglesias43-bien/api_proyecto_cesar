from flask import Blueprint
from controllers.detalles_citas_controllers import (
    cntlistado_detalles, cntlistado_detalles_por_cita, cntcrear_detalle,
    cntactualizar_detalle, cnteliminar_detalle
)

detalle_cita_bp = Blueprint('detalle_cita', __name__)

@detalle_cita_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_detalles()

@detalle_cita_bp.route('/cita/<int:id_cita>', methods=['GET'])
def listado_por_cita(id_cita):
    return cntlistado_detalles_por_cita(id_cita)

@detalle_cita_bp.route('/crear', methods=['POST'])
def crear():
    return cntcrear_detalle()

@detalle_cita_bp.route('/<int:id_detalle>', methods=['PUT'])
def actualizar(id_detalle):
    return cntactualizar_detalle(id_detalle)

@detalle_cita_bp.route('/<int:id_detalle>', methods=['DELETE'])
def eliminar(id_detalle):
    return cnteliminar_detalle(id_detalle)

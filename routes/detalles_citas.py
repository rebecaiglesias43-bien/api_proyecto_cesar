from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.detalles_citas_controllers import (
    cntlistado_detalles, cntlistado_detalles_por_cita, cntcrear_detalle,
    cntactualizar_detalle, cnteliminar_detalle
)

detalle_cita_bp = Blueprint('detalle_cita', __name__)

@detalle_cita_bp.route('/', methods=['GET'])
@jwt_required()
def listado():
    return cntlistado_detalles()

@detalle_cita_bp.route('/cita/<int:id_cita>', methods=['GET'])
@jwt_required()
def listado_por_cita(id_cita):
    return cntlistado_detalles_por_cita(id_cita)

@detalle_cita_bp.route('/crear', methods=['POST'])
@jwt_required()
def crear():
    return cntcrear_detalle()

@detalle_cita_bp.route('/<int:id_detalle>', methods=['PUT'])
@jwt_required()
def actualizar(id_detalle):
    return cntactualizar_detalle(id_detalle)

@detalle_cita_bp.route('/<int:id_detalle>', methods=['DELETE'])
@jwt_required()
def eliminar(id_detalle):
    return cnteliminar_detalle(id_detalle)
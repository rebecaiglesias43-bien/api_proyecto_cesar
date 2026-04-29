from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.citas_controllers import (
    cntlistado_citas, cntobtener_cita, cntcrear_cita,
    cntactualizar_cita, cnteliminar_cita
)

cita_bp = Blueprint('citas', __name__)

@cita_bp.route('/', methods=['GET'])
@jwt_required() 
def listado():
    return cntlistado_citas()

@cita_bp.route('/<int:id_cita>', methods=['GET'])
@jwt_required()
def obtener(id_cita):
    return cntobtener_cita(id_cita)

@cita_bp.route('/crear', methods=['POST'])
@jwt_required()
def crear():
    return cntcrear_cita()

@cita_bp.route('/<int:id_cita>', methods=['PUT'])
@jwt_required()
def actualizar(id_cita):
    return cntactualizar_cita(id_cita)

@cita_bp.route('/<int:id_cita>', methods=['DELETE'])
@jwt_required()
def eliminar(id_cita):
    return cnteliminar_cita(id_cita)
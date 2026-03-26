from flask import Blueprint
from controllers.cita_controllers import (
    cntlistado_citas, cntobtener_cita, cntcrear_cita, 
    cntactualizar_cita, cnteliminar_cita
)

cita_bp = Blueprint('cita', __name__)

@cita_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_citas()

@cita_bp.route('/<int:id_cita>', methods=['GET'])
def obtener(id_cita):
    return cntobtener_cita(id_cita)

@cita_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_cita()

@cita_bp.route('/<int:id_cita>', methods=['PUT'])
def actualizar(id_cita):
    return cntactualizar_cita(id_cita)

@cita_bp.route('/<int:id_cita>', methods=['DELETE'])
def eliminar(id_cita):
    return cnteliminar_cita(id_cita)
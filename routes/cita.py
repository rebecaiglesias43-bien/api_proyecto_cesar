from flask import Blueprint
from controllers.cita_controllers import (
    cntlistado_citas, cntobtener_cita, cntcrear_cita
)

cita_bp = Blueprint('citas', __name__)

@cita_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_citas()

@cita_bp.route('/<int:id_cita>', methods=['GET'])
def obtener(id_cita):
    return cntobtener_cita(id_cita)

@cita_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_cita()
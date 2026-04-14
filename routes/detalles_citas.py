from flask import Blueprint
from controllers.detalles_citas_controllers import (
    cntlistado_detalles, cntlistado_detalles_por_cita, cntcrear_detalle
)

detalle_cita_bp = Blueprint('detalle_cita', __name__)

@detalle_cita_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_detalles()

@detalle_cita_bp.route('/cita/<int:id_cita>', methods=['GET'])
def listado_por_cita(id_cita):
    return cntlistado_detalles_por_cita(id_cita)

@detalle_cita_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_detalle()
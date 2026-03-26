from flask import Blueprint
from controllers.factura_controllers import (
    cntlistado_facturas, cntobtener_factura, 
    cntobtener_factura_por_cita, cntcrear_factura
)

factura_bp = Blueprint('factura', __name__)

@factura_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_facturas()

@factura_bp.route('/<int:id_factura>', methods=['GET'])
def obtener(id_factura):
    return cntobtener_factura(id_factura)

@factura_bp.route('/cita/<int:id_cita>', methods=['GET'])
def obtener_por_cita(id_cita):
    return cntobtener_factura_por_cita(id_cita)

@factura_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_factura()
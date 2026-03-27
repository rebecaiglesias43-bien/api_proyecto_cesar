from flask import Blueprint
from controllers.pago_controllers import (
    cntlistado_pagos, cntobtener_pago, cntlistado_por_factura, cntcrear_pago
)

pago_bp = Blueprint('pago', __name__)

@pago_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_pagos()

@pago_bp.route('/<int:id_pago>', methods=['GET'])
def obtener(id_pago):
    return cntobtener_pago(id_pago)

@pago_bp.route('/factura/<int:id_factura>', methods=['GET'])
def listado_por_factura(id_factura):
    return cntlistado_por_factura(id_factura)

@pago_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_pago()

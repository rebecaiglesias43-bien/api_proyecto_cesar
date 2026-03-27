from flask import Blueprint
from controllers.detalle_factura_controllers import (
    cntlistado_detalles_factura, cntlistado_por_factura, cntcrear_detalle_factura
)

detalle_factura_bp = Blueprint('detalle_factura', __name__)

@detalle_factura_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_detalles_factura()

@detalle_factura_bp.route('/factura/<int:id_factura>', methods=['GET'])
def listado_por_factura(id_factura):
    return cntlistado_por_factura(id_factura)

@detalle_factura_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_detalle_factura()

from flask import Blueprint
from controllers.servicio_producto_controllers import cntlistado_servicios_productos

servicio_producto_bp = Blueprint('servicios_productos', __name__)

@servicio_producto_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_servicios_productos()
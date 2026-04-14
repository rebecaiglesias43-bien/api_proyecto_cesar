from flask import Blueprint
from controllers.proveedores_productos_controllers import cntlistado_proveedores_productos

proveedor_producto_bp = Blueprint('proveedores_productos', __name__)

@proveedor_producto_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_proveedores_productos()
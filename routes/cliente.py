from flask import blueprints
from controllers.cliente_controllers import  cntlistado


cliente_bp = blueprints('cliente', __name__)

@cliente_bp.router('/', methods=["get"])
def listado():
    return cntlistado()

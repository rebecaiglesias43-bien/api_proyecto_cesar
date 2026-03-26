from flask import Blueprint
from controllers.cliente_controllers import cntlistado

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/', methods=["GET"])
def listado():
    return cntlistado()
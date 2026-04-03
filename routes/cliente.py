from flask import Blueprint
from controllers.cliente_controllers import (
    cntlistado_clientes, cntobtener_cliente, cntcrear_cliente
)

cliente_bp = Blueprint('clientes', __name__)

@cliente_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_clientes()

@cliente_bp.route('/<int:id_cliente>', methods=['GET'])
def obtener(id_cliente):
    return cntobtener_cliente(id_cliente)

@cliente_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_cliente()
from flask import Blueprint
from controllers.usuarios_controllers import (
    cntlistado_usuarios, cntobtener_usuario, cntcrear_usuario
)

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_usuarios()

@usuario_bp.route('/<int:id_usuario>', methods=['GET'])
def obtener(id_usuario):
    return cntobtener_usuario(id_usuario)

@usuario_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_usuario()
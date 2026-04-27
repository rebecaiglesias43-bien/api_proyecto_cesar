import os

from flask import Blueprint, current_app, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, verify_jwt_in_request
from controllers.proveedores_controllers import (
    cntlistado_proveedores, cntobtener_proveedor,
    cntcrear_proveedor, cntactualizar_proveedor, cnteliminar_proveedor
)

proveedor_bp = Blueprint('proveedor', __name__)
CORS(proveedor_bp, resources={r"/*": {"origins": "*"}})


def _ensure_jwt():
    app = current_app._get_current_object()
    if not app.config.get('JWT_SECRET_KEY'):
        app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or os.getenv('SECRET_KEY') or 'change-me'
    if 'jwt' not in app.extensions:
        JWTManager(app)


@proveedor_bp.before_request
def _protect_routes():
    if request.method == 'OPTIONS':
        return None
    _ensure_jwt()
    verify_jwt_in_request()

@proveedor_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_proveedores()

@proveedor_bp.route('/<int:id_proveedor>', methods=['GET'])
def obtener(id_proveedor):
    return cntobtener_proveedor(id_proveedor)

@proveedor_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_proveedor()

@proveedor_bp.route('/<int:id_proveedor>', methods=['PUT'])
def actualizar(id_proveedor):
    return cntactualizar_proveedor(id_proveedor)

@proveedor_bp.route('/<int:id_proveedor>', methods=['DELETE'])
def eliminar(id_proveedor):
    return cnteliminar_proveedor(id_proveedor)

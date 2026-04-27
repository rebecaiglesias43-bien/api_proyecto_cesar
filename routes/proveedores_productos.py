import os

from flask import Blueprint, current_app, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, verify_jwt_in_request
from controllers.proveedores_productos_controllers import (
    cntlistado_proveedores_productos,
    cntobtener_proveedor_producto,
    cntcrear_proveedor_producto,
    cntactualizar_proveedor_producto,
    cnteliminar_proveedor_producto
)

proveedor_producto_bp = Blueprint('proveedores_productos', __name__)
CORS(proveedor_producto_bp, resources={r"/*": {"origins": "*"}})


def _ensure_jwt():
    app = current_app._get_current_object()
    if not app.config.get('JWT_SECRET_KEY'):
        app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or os.getenv('SECRET_KEY') or 'change-me'
    if 'jwt' not in app.extensions:
        JWTManager(app)


@proveedor_producto_bp.before_request
def _protect_routes():
    if request.method == 'OPTIONS':
        return None
    _ensure_jwt()
    verify_jwt_in_request()


@proveedor_producto_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_proveedores_productos()


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['GET'])
def obtener(id_relacion):
    return cntobtener_proveedor_producto(id_relacion)


@proveedor_producto_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_proveedor_producto()


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['PUT'])
def actualizar(id_relacion):
    return cntactualizar_proveedor_producto(id_relacion)


@proveedor_producto_bp.route('/<int:id_relacion>', methods=['DELETE'])
def eliminar(id_relacion):
    return cnteliminar_proveedor_producto(id_relacion)

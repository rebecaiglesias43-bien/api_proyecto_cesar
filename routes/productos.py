import os

from flask import Blueprint, current_app, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, verify_jwt_in_request
from controllers.productos_controllers import (
    cntlistado_productos, cntobtener_producto, cntcrear_producto
)

producto_bp = Blueprint('productos', __name__)
CORS(producto_bp, resources={r"/*": {"origins": "*"}})


def _ensure_jwt():
    app = current_app._get_current_object()
    if not app.config.get('JWT_SECRET_KEY'):
        app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or os.getenv('SECRET_KEY') or 'change-me'
    if 'jwt' not in app.extensions:
        JWTManager(app)


@producto_bp.before_request
def _protect_routes():
    if request.method == 'OPTIONS':
        return None
    _ensure_jwt()
    verify_jwt_in_request()

@producto_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_productos()

@producto_bp.route('/<int:id_producto>', methods=['GET'])
def obtener(id_producto):
    return cntobtener_producto(id_producto)

@producto_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_producto()

from flask import Blueprint
from controllers.empleados_controllers import (
    cntlistado_empleados, cntobtener_empleado, cntcrear_empleado
)

empleado_bp = Blueprint('empleados', __name__)

@empleado_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_empleados()

@empleado_bp.route('/<int:id_empleado>', methods=['GET'])
def obtener(id_empleado):
    return cntobtener_empleado(id_empleado)

@empleado_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_empleado()
from flask import Blueprint
from controllers.horario_controllers import (
    cntlistado_horarios, cntlistado_por_empleado, cntcrear_horario
)

horario_bp = Blueprint('horarios', __name__)

@horario_bp.route('/', methods=['GET'])
def listado():
    return cntlistado_horarios()

@horario_bp.route('/empleado/<int:id_empleado>', methods=['GET'])
def listado_por_empleado(id_empleado):
    return cntlistado_por_empleado(id_empleado)

@horario_bp.route('/', methods=['POST'])
def crear():
    return cntcrear_horario()
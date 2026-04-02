from flask import request, jsonify, current_app
from services.empleado_services import EmpleadoService

def cntlistado_empleados():
    service = EmpleadoService(current_app.mysql)
    return jsonify(service.listar_todos())

def cntobtener_empleado(id_empleado):
    service = EmpleadoService(current_app.mysql)
    empleado = service.obtener_por_id(id_empleado)
    if empleado:
        return jsonify(empleado)
    return jsonify({'error': 'Empleado no encontrado'}), 404

def cntcrear_empleado():
    data = request.get_json()
    service = EmpleadoService(current_app.mysql)
    empleado = service.crear(
        id_usuario=data.get('id_usuario'),
        nombre=data.get('nombre'),
        apellido=data.get('apellido'),
        telefono=data.get('telefono'),
        cargo=data.get('cargo'),
        especialidad=data.get('especialidad')
    )
    return jsonify(empleado), 201
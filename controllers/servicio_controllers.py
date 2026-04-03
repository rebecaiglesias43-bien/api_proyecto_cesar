from flask import jsonify, request, current_app
import traceback

def cntlistado_servicios():
    try:
        from services.servicio_services import ServicioService
        service = ServicioService(current_app.mysql)
        return jsonify(service.listar_todos())
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntobtener_servicio(id_servicio):
    try:
        from services.servicio_services import ServicioService
        service = ServicioService(current_app.mysql)
        servicio = service.obtener_por_id(id_servicio)
        if servicio:
            return jsonify(servicio)
        return jsonify({'error': 'Servicio no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cntcrear_servicio():
    try:
        data = request.get_json()
        from services.servicio_services import ServicioService
        service = ServicioService(current_app.mysql)
        servicio = service.crear(
            nombre_servicio=data.get('nombre_servicio'),
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            duracion_aprox=data.get('duracion_aprox')
        )
        return jsonify(servicio), 201
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntactualizar_servicio(id_servicio):
    try:
        data = request.get_json()
        from services.servicio_services import ServicioService
        service = ServicioService(current_app.mysql)
        servicio = service.actualizar(
            id_servicio,
            nombre_servicio=data.get('nombre_servicio'),
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            duracion_aprox=data.get('duracion_aprox')
        )
        if servicio:
            return jsonify(servicio)
        return jsonify({'error': 'Servicio no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cnteliminar_servicio(id_servicio):
    try:
        from services.servicio_services import ServicioService
        service = ServicioService(current_app.mysql)
        if service.eliminar(id_servicio):
            return jsonify({'mensaje': 'Servicio eliminado correctamente'})
        return jsonify({'error': 'Servicio no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

from flask import jsonify, request, current_app
import traceback

def cntlistado_citas():
    try:
        from services.cita_service import CitaService
        service = CitaService(current_app.mysql)
        return jsonify(service.listar_todas())
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntobtener_cita(id_cita):
    try:
        from services.cita_service import CitaService
        service = CitaService(current_app.mysql)
        cita = service.obtener_por_id(id_cita)
        if cita:
            return jsonify(cita)
        return jsonify({'error': 'Cita no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cntcrear_cita():
    try:
        data = request.get_json()
        from services.cita_service import CitaService
        service = CitaService(current_app.mysql)
        cita = service.crear(
            id_cliente=data.get('id_cliente'),
            id_empleado=data.get('id_empleado'),
            fecha=data.get('fecha'),
            hora=data.get('hora'),
            estado=data.get('estado', 'pendiente')
        )
        return jsonify(cita), 201
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntactualizar_cita(id_cita):
    try:
        data = request.get_json()
        from services.cita_service import CitaService
        service = CitaService(current_app.mysql)
        cita = service.actualizar(
            id_cita,
            id_cliente=data.get('id_cliente'),
            id_empleado=data.get('id_empleado'),
            fecha=data.get('fecha'),
            hora=data.get('hora'),
            estado=data.get('estado')
        )
        if cita:
            return jsonify(cita)
        return jsonify({'error': 'Cita no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cnteliminar_cita(id_cita):
    try:
        from services.cita_service import CitaService
        service = CitaService(current_app.mysql)
        if service.eliminar(id_cita):
            return jsonify({'mensaje': 'Cita eliminada correctamente'})
        return jsonify({'error': 'Cita no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
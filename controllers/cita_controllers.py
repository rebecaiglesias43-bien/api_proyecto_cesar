from flask import jsonify, request, current_app
import traceback

def cntlistado_citas():
    try:
        from services.cita_service import CitaService
        service = CitaService(current_app.mysql)
        citas = service.listar_todas()
        return jsonify(citas)
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
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntcrear_cita():
    try:
        data = request.get_json()
        from services.cita_service import CitaService
        service = CitaService(current_app.mysql)
        cita = service.crear(
            fecha=data.get('fecha'),
            hora=data.get('hora'),
            estado=data.get('estado', 'pendiente'),
            id_clienteFK=data.get('id_clienteFK'),
            id_empleadoFK=data.get('id_empleadoFK')
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
            fecha=data.get('fecha'),
            hora=data.get('hora'),
            estado=data.get('estado'),
            id_clienteFK=data.get('id_clienteFK'),
            id_empleadoFK=data.get('id_empleadoFK')
        )
        if cita:
            return jsonify(cita)
        return jsonify({'error': 'Cita no encontrada'}), 404
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cnteliminar_cita(id_cita):
    try:
        from services.cita_service import CitaService
        service = CitaService(current_app.mysql)
        eliminado = service.eliminar(id_cita)
        if eliminado:
            return jsonify({'mensaje': 'Cita eliminada correctamente'})
        return jsonify({'error': 'Cita no encontrada'}), 404
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
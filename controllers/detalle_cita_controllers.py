from flask import jsonify, request, current_app
import traceback

def cntlistado_detalles():
    try:
        from services.detalle_cita_service import DetalleCitaService
        service = DetalleCitaService(current_app.mysql)
        detalles = service.listar_todos()
        return jsonify(detalles)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntlistado_detalles_por_cita(id_cita):
    try:
        from services.detalle_cita_service import DetalleCitaService
        service = DetalleCitaService(current_app.mysql)
        detalles = service.listar_por_cita(id_cita)
        return jsonify(detalles)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntcrear_detalle():
    try:
        data = request.get_json()
        from services.detalle_cita_service import DetalleCitaService
        service = DetalleCitaService(current_app.mysql)
        detalle = service.crear(
            id_citaFK=data.get('id_citaFK'),
            id_servicioFK=data.get('id_servicioFK'),
            precio_servicio=data.get('precio_servicio')
        )
        return jsonify(detalle), 201
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
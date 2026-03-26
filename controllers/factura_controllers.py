from flask import jsonify, request, current_app
import traceback

def cntlistado_facturas():
    try:
        from services.factura_service import FacturaService
        service = FacturaService(current_app.mysql)
        facturas = service.listar_todas()
        return jsonify(facturas)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntobtener_factura(id_factura):
    try:
        from services.factura_service import FacturaService
        service = FacturaService(current_app.mysql)
        factura = service.obtener_por_id(id_factura)
        if factura:
            return jsonify(factura)
        return jsonify({'error': 'Factura no encontrada'}), 404
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntobtener_factura_por_cita(id_cita):
    try:
        from services.factura_service import FacturaService
        service = FacturaService(current_app.mysql)
        factura = service.obtener_por_cita(id_cita)
        if factura:
            return jsonify(factura)
        return jsonify({'error': 'Factura no encontrada para esta cita'}), 404
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntcrear_factura():
    try:
        data = request.get_json()
        from services.factura_service import FacturaService
        service = FacturaService(current_app.mysql)
        factura = service.crear(
            id_citaFK=data.get('id_citaFK'),
            total=data.get('total')
        )
        return jsonify(factura), 201
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
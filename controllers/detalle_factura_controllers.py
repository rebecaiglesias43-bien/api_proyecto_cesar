from flask import jsonify, request, current_app
import traceback

def cntlistado_detalles_factura():
    try:
        from services.detalle_factura_service import DetalleFacturaService
        service = DetalleFacturaService(current_app.mysql)
        return jsonify(service.listar_todos())
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntlistado_por_factura(id_factura):
    try:
        from services.detalle_factura_service import DetalleFacturaService
        service = DetalleFacturaService(current_app.mysql)
        return jsonify(service.listar_por_factura(id_factura))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cntcrear_detalle_factura():
    try:
        data = request.get_json()
        from services.detalle_factura_service import DetalleFacturaService
        service = DetalleFacturaService(current_app.mysql)
        detalle = service.crear(
            id_factura=data.get('id_factura'),
            id_servicio=data.get('id_servicio'),
            subtotal=data.get('subtotal')
        )
        return jsonify(detalle), 201
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

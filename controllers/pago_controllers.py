from flask import jsonify, request, current_app
import traceback

def cntlistado_pagos():
    try:
        from services.pago_service import PagoService
        service = PagoService(current_app.mysql)
        return jsonify(service.listar_todos())
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntobtener_pago(id_pago):
    try:
        from services.pago_service import PagoService
        service = PagoService(current_app.mysql)
        pago = service.obtener_por_id(id_pago)
        if pago:
            return jsonify(pago)
        return jsonify({'error': 'Pago no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cntlistado_por_factura(id_factura):
    try:
        from services.pago_service import PagoService
        service = PagoService(current_app.mysql)
        return jsonify(service.listar_por_factura(id_factura))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cntcrear_pago():
    try:
        data = request.get_json()
        from services.pago_service import PagoService
        service = PagoService(current_app.mysql)
        pago = service.crear(
            id_factura=data.get('id_factura'),
            metodo_pago=data.get('metodo_pago'),
            monto=data.get('monto')
        )
        return jsonify(pago), 201
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

from flask import jsonify, request, current_app
import traceback

def cntlistado_proveedores():
    try:
        from services.proveedor_service import ProveedorService
        service = ProveedorService(current_app.mysql)
        proveedores = service.listar_todos()
        return jsonify(proveedores)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntobtener_proveedor(id_proveedor):
    try:
        from services.proveedor_service import ProveedorService
        service = ProveedorService(current_app.mysql)
        proveedor = service.obtener_por_id(id_proveedor)
        if proveedor:
            return jsonify(proveedor)
        return jsonify({'error': 'Proveedor no encontrado'}), 404
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntcrear_proveedor():
    try:
        data = request.get_json()
        from services.proveedor_service import ProveedorService
        service = ProveedorService(current_app.mysql)
        proveedor = service.crear(
            nombre_contacto=data.get('nombre_contacto'),
            empresa=data.get('empresa'),
            telefono=data.get('telefono')
        )
        return jsonify(proveedor), 201
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cntactualizar_proveedor(id_proveedor):
    try:
        data = request.get_json()
        from services.proveedor_service import ProveedorService
        service = ProveedorService(current_app.mysql)
        proveedor = service.actualizar(
            id_proveedor,
            nombre_contacto=data.get('nombre_contacto'),
            empresa=data.get('empresa'),
            telefono=data.get('telefono')
        )
        if proveedor:
            return jsonify(proveedor)
        return jsonify({'error': 'Proveedor no encontrado'}), 404
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def cnteliminar_proveedor(id_proveedor):
    try:
        from services.proveedor_service import ProveedorService
        service = ProveedorService(current_app.mysql)
        eliminado = service.eliminar(id_proveedor)
        if eliminado:
            return jsonify({'mensaje': 'Proveedor eliminado correctamente'})
        return jsonify({'error': 'Proveedor no encontrado'}), 404
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
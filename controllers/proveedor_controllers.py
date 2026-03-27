from flask import jsonify, request, current_app
import traceback

def cntlistado_proveedores():
    try:
        from services.proveedor_service import ProveedorService
        service = ProveedorService(current_app.mysql)
        return jsonify(service.listar_todos())
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
        return jsonify({'error': str(e)}), 500

def cntcrear_proveedor():
    try:
        data = request.get_json()
        from services.proveedor_service import ProveedorService
        service = ProveedorService(current_app.mysql)
        proveedor = service.crear(
            nombre_proveedor=data.get('nombre_proveedor'),
            telefono=data.get('telefono'),
            correo=data.get('correo'),
            direccion=data.get('direccion')
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
            nombre_proveedor=data.get('nombre_proveedor'),
            telefono=data.get('telefono'),
            correo=data.get('correo'),
            direccion=data.get('direccion')
        )
        if proveedor:
            return jsonify(proveedor)
        return jsonify({'error': 'Proveedor no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cnteliminar_proveedor(id_proveedor):
    try:
        from services.proveedor_service import ProveedorService
        service = ProveedorService(current_app.mysql)
        if service.eliminar(id_proveedor):
            return jsonify({'mensaje': 'Proveedor eliminado correctamente'})
        return jsonify({'error': 'Proveedor no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
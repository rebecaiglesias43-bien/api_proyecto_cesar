import re

from flask import request, jsonify, current_app
from services.proveedores_services import ProveedorService


EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
TELEFONO_REGEX = re.compile(r"^[0-9+\-\s()]+$")
NOMBRE_REGEX = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$")


def _validar_texto(data, campo, requerido=False, max_length=None):
    valor = data.get(campo)

    if valor is None:
        if requerido:
            return None, f'El campo "{campo}" es requerido'
        return None, None

    if not isinstance(valor, str):
        return None, f'El campo "{campo}" debe ser una cadena de texto'

    valor = valor.strip()
    if requerido and not valor:
        return None, f'El campo "{campo}" es requerido'

    if not valor:
        return None, None

    if max_length is not None and len(valor) > max_length:
        return None, f'El campo "{campo}" supera el maximo de {max_length} caracteres'

    return valor, None


def _validar_payload_proveedor(data):
    if not isinstance(data, dict):
        return None, ('El cuerpo de la solicitud debe ser un objeto JSON', 400)

    nombre, error = _validar_texto(data, 'nombre', requerido=True, max_length=100)
    if error:
        return None, (error, 400)
    if not NOMBRE_REGEX.fullmatch(nombre):
        return None, ('El campo "nombre" solo puede contener letras y espacios', 400)

    telefono, error = _validar_texto(data, 'telefono', max_length=20)
    if error:
        return None, (error, 400)
    if telefono and not TELEFONO_REGEX.fullmatch(telefono):
        return None, ('El campo "telefono" tiene un formato invalido', 400)

    email, error = _validar_texto(data, 'email', max_length=100)
    if error:
        return None, (error, 400)
    if email and not EMAIL_REGEX.fullmatch(email):
        return None, ('El campo "email" tiene un formato invalido', 400)

    direccion, error = _validar_texto(data, 'direccion', max_length=150)
    if error:
        return None, (error, 400)

    return {
        'nombre': nombre,
        'telefono': telefono,
        'email': email,
        'direccion': direccion
    }, None


def cntlistado_proveedores():
    service = ProveedorService(current_app.mysql)
    return jsonify(service.listar_todos())


def cntobtener_proveedor(id_proveedor):
    service = ProveedorService(current_app.mysql)
    proveedor = service.obtener_por_id(id_proveedor)
    if proveedor:
        return jsonify(proveedor)
    return jsonify({'error': 'Proveedor no encontrado'}), 404


def cntcrear_proveedor():
    data = request.get_json(silent=True) or {}
    payload, error = _validar_payload_proveedor(data)
    if error:
        return jsonify({'error': error[0]}), error[1]

    service = ProveedorService(current_app.mysql)
    proveedor = service.crear(
        nombre=payload['nombre'],
        telefono=payload['telefono'],
        email=payload['email'],
        direccion=payload['direccion']
    )
    return jsonify(proveedor), 201


def cntactualizar_proveedor(id_proveedor):
    data = request.get_json(silent=True) or {}
    payload, error = _validar_payload_proveedor(data)
    if error:
        return jsonify({'error': error[0]}), error[1]

    service = ProveedorService(current_app.mysql)
    proveedor = service.actualizar(
        id_proveedor=id_proveedor,
        nombre=payload['nombre'],
        telefono=payload['telefono'],
        email=payload['email'],
        direccion=payload['direccion']
    )
    if proveedor:
        return jsonify(proveedor)
    return jsonify({'error': 'Proveedor no encontrado'}), 404


def cnteliminar_proveedor(id_proveedor):
    service = ProveedorService(current_app.mysql)
    try:
        if service.eliminar(id_proveedor):
            return jsonify({'mensaje': 'Proveedor eliminado'})
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    return jsonify({'error': 'Proveedor no encontrado'}), 404

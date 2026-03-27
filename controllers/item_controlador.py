from flask import request, jsonify
from servicios.item_servicio import *

def listar_items():
    return jsonify(listar_items_servicio())

def obtener_item(id_item):
    item = obtener_item_servicio(id_item)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item no encontrado"}), 404

def crear_item():
    data = request.json
    return jsonify(crear_item_servicio(data))

def actualizar_item(id_item):
    data = request.json
    return jsonify(actualizar_item_servicio(id_item, data))

def eliminar_item(id_item):
    return jsonify(eliminar_item_servicio(id_item))

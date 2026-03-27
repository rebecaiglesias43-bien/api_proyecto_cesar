from flask import request, jsonify
from modelos.item_modelo import ItemModel

def listar_items():
    return jsonify(ItemModel.get_all())

def obtener_item(id_item):
    item = ItemModel.get_by_id(id_item)
    if item:
        return jsonify(item)
    return jsonify({"error": "No encontrado"}), 404

def crear_item():
    data = request.json
    return jsonify(ItemModel.create(data))

def actualizar_item(id_item):
    data = request.json
    return jsonify(ItemModel.update(id_item, data))

def eliminar_item(id_item):
    return jsonify(ItemModel.delete(id_item))

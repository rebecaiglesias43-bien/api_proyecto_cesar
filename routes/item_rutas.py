from flask import Blueprint
from controladores.item_controlador import *

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/items', methods=['GET'])
def listar_items_ruta():
    return listar_items()

@item_bp.route('/items/<int:id_item>', methods=['GET'])
def obtener_item_ruta(id_item):
    return obtener_item(id_item)

@item_bp.route('/items', methods=['POST'])
def crear_item_ruta():
    return crear_item()

@item_bp.route('/items/<int:id_item>', methods=['PUT'])
def actualizar_item_ruta(id_item):
    return actualizar_item(id_item)

@item_bp.route('/items/<int:id_item>', methods=['DELETE'])
def eliminar_item_ruta(id_item):
    return eliminar_item(id_item)

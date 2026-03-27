from modelos.item_modelo import ItemModel

def listar_items_servicio():
    return ItemModel.get_all()

def obtener_item_servicio(id_item):
    return ItemModel.get_by_id(id_item)

def crear_item_servicio(data):
    # aquí podrías validar datos si quieres
    return ItemModel.create(data)

def actualizar_item_servicio(id_item, data):
    return ItemModel.update(id_item, data)

def eliminar_item_servicio(id_item):
    return ItemModel.delete(id_item)

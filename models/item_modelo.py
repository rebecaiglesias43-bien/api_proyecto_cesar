class ItemModel:
    def __init__(self, id_item, nombre, precio, cantidad_stock, estado):
        self.id_item = id_item
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.estado = estado

    def to_dict(self):
        return {
            "id_item": self.id_item,
            "nombre": self.nombre,
            "precio": float(self.precio) if self.precio else 0,
            "cantidad_stock": self.cantidad_stock,
            "estado": self.estado
        }

from flask import current_app

class ProveedorProductoModel:
    def __init__(self, id_relacion=None, id_proveedor=None, id_producto=None, precio=None):
        self.id_relacion = id_relacion
        self.id_proveedor = id_proveedor
        self.id_producto = id_producto
        self.precio = precio

    def to_dict(self):
        return {
            'id_relacion': self.id_relacion,
            'id_proveedor': self.id_proveedor,
            'id_producto': self.id_producto,
            'precio': float(self.precio) if self.precio else None
        }

    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT ppr_id, ppr_proveedor_id, ppr_producto_id, ppr_precio FROM proveedores_productos")
        datos = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in datos:
            resultado.append(ProveedorProductoModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
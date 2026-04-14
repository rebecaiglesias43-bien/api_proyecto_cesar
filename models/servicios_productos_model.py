from flask import current_app

class ServicioProductoModel:
    def __init__(self, id_relacion=None, id_servicio=None, id_producto=None, cantidad=None):
        self.id_relacion = id_relacion
        self.id_servicio = id_servicio
        self.id_producto = id_producto
        self.cantidad = cantidad

    def to_dict(self):
        return {
            'id_relacion': self.id_relacion,
            'id_servicio': self.id_servicio,
            'id_producto': self.id_producto,
            'cantidad': self.cantidad
        }

    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT sep_id, sep_servicio_id, sep_producto_id, sep_cantidad FROM servicios_productos")
        datos = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in datos:
            resultado.append(ServicioProductoModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
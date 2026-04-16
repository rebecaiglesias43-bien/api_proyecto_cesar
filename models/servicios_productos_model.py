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

    @staticmethod
    def obtener_por_id(id_relacion):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT sep_id, sep_servicio_id, sep_producto_id, sep_cantidad FROM servicios_productos WHERE sep_id = %s", (id_relacion,))
        d = cursor.fetchone()
        cursor.close()
        if d:
            return ServicioProductoModel(d[0], d[1], d[2], d[3]).to_dict()
        return None

    @staticmethod
    def crear(id_servicio, id_producto, cantidad):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO servicios_productos (sep_servicio_id, sep_producto_id, sep_cantidad) VALUES (%s, %s, %s)",
            (id_servicio, id_producto, cantidad)
        )
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return ServicioProductoModel.obtener_por_id(id_generado)

    @staticmethod
    def actualizar(id_relacion, id_servicio, id_producto, cantidad):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE servicios_productos SET sep_servicio_id = %s, sep_producto_id = %s, sep_cantidad = %s WHERE sep_id = %s",
            (id_servicio, id_producto, cantidad, id_relacion)
        )
        current_app.mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        if filas == 0:
            return None
        return ServicioProductoModel.obtener_por_id(id_relacion)

    @staticmethod
    def eliminar(id_relacion):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM servicios_productos WHERE sep_id = %s", (id_relacion,))
        current_app.mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        return filas > 0
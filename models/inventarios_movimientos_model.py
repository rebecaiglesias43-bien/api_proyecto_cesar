from flask import current_app

class InventarioMovimientoModel:
    def __init__(self, id_movimiento=None, id_producto=None, tipo=None, cantidad=None, fecha=None, motivo=None):
        self.id_movimiento = id_movimiento
        self.id_producto = id_producto
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha
        self.motivo = motivo

    def to_dict(self):
        return {
            'id_movimiento': self.id_movimiento,
            'id_producto': self.id_producto,
            'tipo': self.tipo,
            'cantidad': self.cantidad,
            'fecha': str(self.fecha) if self.fecha else None,
            'motivo': self.motivo
        }

    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT inm_id, inm_producto_id, inm_tipo, inm_cantidad, inm_fecha, inm_motivo FROM inventario_movimientos")
        datos = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in datos:
            resultado.append(InventarioMovimientoModel(d[0], d[1], d[2], d[3], d[4], d[5]).to_dict())
        return resultado
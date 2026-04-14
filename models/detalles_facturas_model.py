from flask import current_app

class DetalleFacturaModel:
    def __init__(self, id_detalle=None, id_factura=None, id_servicio=None, subtotal=None):
        self.id_detalle = id_detalle
        self.id_factura = id_factura
        self.id_servicio = id_servicio
        self.subtotal = subtotal
    
    def to_dict(self):
        return {
            'id_detalle': self.id_detalle,
            'id_factura': self.id_factura,
            'id_servicio': self.id_servicio,
            'subtotal': float(self.subtotal) if self.subtotal else None
        }
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dfa_id, dfa_factura_id, dfa_servicio_id, dfa_subtotal FROM detalle_facturas")
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in detalles:
            resultado.append(DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
    
    @staticmethod
    def listar_por_factura(id_factura):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dfa_id, dfa_factura_id, dfa_servicio_id, dfa_subtotal FROM detalle_facturas WHERE dfa_factura_id = %s", (id_factura,))
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in detalles:
            resultado.append(DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
    
    @staticmethod
    def crear(id_factura, id_servicio, subtotal):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO detalle_facturas (dfa_factura_id, dfa_servicio_id, dfa_subtotal) VALUES (%s, %s, %s)", (id_factura, id_servicio, subtotal))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dfa_id, dfa_factura_id, dfa_servicio_id, dfa_subtotal FROM detalle_facturas WHERE dfa_id = %s", (id_generado,))
        d = cursor.fetchone()
        cursor.close()
        if d:
            return DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict()
        return None
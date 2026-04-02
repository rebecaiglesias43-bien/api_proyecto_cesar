from models.detalle_factura_model import DetalleFacturaModel

class DetalleFacturaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_detalle, id_factura, id_servicio, subtotal FROM detalle_facturas")
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in detalles:
            resultado.append(DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
    
    def listar_por_factura(self, id_factura):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_detalle, id_factura, id_servicio, subtotal FROM detalle_facturas WHERE id_factura = %s", (id_factura,))
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in detalles:
            resultado.append(DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
    
    def crear(self, id_factura, id_servicio, subtotal):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO detalle_facturas (id_factura, id_servicio, subtotal) VALUES (%s, %s, %s)",
            (id_factura, id_servicio, subtotal)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_detalle, id_factura, id_servicio, subtotal FROM detalle_facturas WHERE id_detalle = %s", (id_generado,))
        d = cursor.fetchone()
        cursor.close()
        if d:
            return DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict()
        return None
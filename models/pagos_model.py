from flask import current_app

class PagoModel:
    def __init__(self, id_pago=None, id_factura=None, metodo=None, fecha=None, monto=None):
        self.id_pago = id_pago
        self.id_factura = id_factura
        self.metodo = metodo
        self.fecha = fecha
        self.monto = monto
    
    def to_dict(self):
        return {
            'id_pago': self.id_pago,
            'id_factura': self.id_factura,
            'metodo': self.metodo,
            'fecha': str(self.fecha) if self.fecha else None,
            'monto': float(self.monto) if self.monto else None
        }
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT pag_id, pag_factura_id, pag_metodo, pag_fecha, pag_monto FROM pagos")
        pagos = cursor.fetchall()
        cursor.close()
        resultado = []
        for p in pagos:
            resultado.append(PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_pago):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT pag_id, pag_factura_id, pag_metodo, pag_fecha, pag_monto FROM pagos WHERE pag_id = %s", (id_pago,))
        p = cursor.fetchone()
        cursor.close()
        if p:
            return PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict()
        return None
    
    @staticmethod
    def listar_por_factura(id_factura):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT pag_id, pag_factura_id, pag_metodo, pag_fecha, pag_monto FROM pagos WHERE pag_factura_id = %s", (id_factura,))
        pagos = cursor.fetchall()
        cursor.close()
        resultado = []
        for p in pagos:
            resultado.append(PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict())
        return resultado
    
    @staticmethod
    def crear(id_factura, metodo, fecha, monto):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO pagos (pag_factura_id, pag_metodo, pag_fecha, pag_monto) VALUES (%s, %s, %s, %s)", (id_factura, metodo, fecha, monto))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return PagoModel.obtener_por_id(id_generado)
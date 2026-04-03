from flask import current_app

class FacturaModel:
    def __init__(self, id_factura=None, id_cita=None, fecha=None, total=None, estado=None):
        self.id_factura = id_factura
        self.id_cita = id_cita
        self.fecha = fecha
        self.total = total
        self.estado = estado
    
    def to_dict(self):
        return {
            'id_factura': self.id_factura,
            'id_cita': self.id_cita,
            'fecha': str(self.fecha) if self.fecha else None,
            'total': float(self.total) if self.total else None,
            'estado': self.estado
        }
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT fac_id, fac_cita_id, fac_fecha, fac_total, fac_estado FROM facturas")
        facturas = cursor.fetchall()
        cursor.close()
        resultado = []
        for f in facturas:
            resultado.append(FacturaModel(f[0], f[1], f[2], f[3], f[4]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_factura):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT fac_id, fac_cita_id, fac_fecha, fac_total, fac_estado FROM facturas WHERE fac_id = %s", (id_factura,))
        f = cursor.fetchone()
        cursor.close()
        if f:
            return FacturaModel(f[0], f[1], f[2], f[3], f[4]).to_dict()
        return None
    
    @staticmethod
    def crear(id_cita, fecha, total, estado):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO facturas (fac_cita_id, fac_fecha, fac_total, fac_estado) VALUES (%s, %s, %s, %s)", (id_cita, fecha, total, estado))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return FacturaModel.obtener_por_id(id_generado)
from models.factura_model import FacturaModel
from datetime import date

class FacturaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todas(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_factura, id_cita, fecha, total, estado FROM factura")
        facturas = cursor.fetchall()
        cursor.close()
        resultado = []
        for factura in facturas:
            resultado.append(FacturaModel(factura[0], factura[1], factura[2], factura[3], factura[4]).to_dict())
        return resultado
    
    def obtener_por_id(self, id_factura):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_factura, id_cita, fecha, total, estado FROM factura WHERE id_factura = %s", (id_factura,))
        factura = cursor.fetchone()
        cursor.close()
        if factura:
            return FacturaModel(factura[0], factura[1], factura[2], factura[3], factura[4]).to_dict()
        return None
    
    def obtener_por_cita(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_factura, id_cita, fecha, total, estado FROM factura WHERE id_cita = %s", (id_cita,))
        factura = cursor.fetchone()
        cursor.close()
        if factura:
            return FacturaModel(factura[0], factura[1], factura[2], factura[3], factura[4]).to_dict()
        return None
    
    def crear(self, id_cita, total, estado='pendiente'):
        fecha_actual = date.today()
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO factura (id_cita, fecha, total, estado) VALUES (%s, %s, %s, %s)",
            (id_cita, fecha_actual, total, estado)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
    
    def actualizar_estado(self, id_factura, estado):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "UPDATE factura SET estado = %s WHERE id_factura = %s",
            (estado, id_factura)
        )
        self.mysql.connection.commit()
        cursor.close()
        return self.obtener_por_id(id_factura)
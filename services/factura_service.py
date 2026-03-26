from models.factura_model import FacturaModel
from datetime import datetime

class FacturaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todas(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM factura")
        facturas = cursor.fetchall()
        cursor.close()
        
        resultado = []
        for factura in facturas:
            resultado.append(FacturaModel(
                factura[0], factura[1], factura[2], factura[3]
            ).to_dict())
        return resultado
    
    def obtener_por_id(self, id_factura):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM factura WHERE id_factura = %s", (id_factura,))
        factura = cursor.fetchone()
        cursor.close()
        
        if factura:
            return FacturaModel(factura[0], factura[1], factura[2], factura[3]).to_dict()
        return None
    
    def obtener_por_cita(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM factura WHERE id_citaFK = %s", (id_cita,))
        factura = cursor.fetchone()
        cursor.close()
        
        if factura:
            return FacturaModel(factura[0], factura[1], factura[2], factura[3]).to_dict()
        return None
    
    def crear(self, id_citaFK, total):
        fecha_actual = datetime.now()
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO factura (id_citaFK, total, fecha_emision) VALUES (%s, %s, %s)",
            (id_citaFK, total, fecha_actual)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
    
    def actualizar_total(self, id_factura, total):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "UPDATE factura SET total = %s WHERE id_factura = %s",
            (total, id_factura)
        )
        self.mysql.connection.commit()
        cursor.close()
        return self.obtener_por_id(id_factura)
from models.pago_model import PagoModel
from datetime import date

class PagoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_pago, id_factura, metodo_pago, fecha_pago, monto FROM pagos")
        pagos = cursor.fetchall()
        cursor.close()
        resultado = []
        for p in pagos:
            resultado.append(PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict())
        return resultado
    
    def obtener_por_id(self, id_pago):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_pago, id_factura, metodo_pago, fecha_pago, monto FROM pagos WHERE id_pago = %s", (id_pago,))
        p = cursor.fetchone()
        cursor.close()
        if p:
            return PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict()
        return None
        
    def listar_por_factura(self, id_factura):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_pago, id_factura, metodo_pago, fecha_pago, monto FROM pagos WHERE id_factura = %s", (id_factura,))
        pagos = cursor.fetchall()
        cursor.close()
        resultado = []
        for p in pagos:
            resultado.append(PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict())
        return resultado
    
    def crear(self, id_factura, metodo_pago, monto):
        fecha_actual = date.today()
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO pagos (id_factura, metodo_pago, fecha_pago, monto) VALUES (%s, %s, %s, %s)",
            (id_factura, metodo_pago, fecha_actual, monto)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
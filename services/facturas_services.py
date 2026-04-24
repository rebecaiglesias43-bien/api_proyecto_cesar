from models.facturas_model import FacturaModel
from datetime import date

class FacturaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todas(self):
        return FacturaModel.listar_todos()
    
    def obtener_por_id(self, id_factura):
        return FacturaModel.obtener_por_id(id_factura)
    
    def obtener_por_cita(self, id_cita):
        return FacturaModel.obtener_por_cita(id_cita)
    
    def crear(self, id_cita, total, estado='pendiente'):
        fecha_actual = date.today()
        return FacturaModel.crear(id_cita, fecha_actual, total, estado)
    
    def actualizar_estado(self, id_factura, estado):
        return FacturaModel.actualizar_estado(id_factura, estado)
    
    def actualizar(self, id_factura, **datos):
        return FacturaModel.actualizar(id_factura, **datos)
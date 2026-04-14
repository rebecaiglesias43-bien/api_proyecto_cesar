from models.pagos_model import PagoModel
from datetime import date

class PagoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return PagoModel.listar_todos()
    
    def obtener_por_id(self, id_pago):
        return PagoModel.obtener_por_id(id_pago)
    
    def listar_por_factura(self, id_factura):
        return PagoModel.listar_por_factura(id_factura)
    
    def crear(self, id_factura, metodo, monto):
        fecha_actual = date.today()
        return PagoModel.crear(id_factura, metodo, fecha_actual, monto)
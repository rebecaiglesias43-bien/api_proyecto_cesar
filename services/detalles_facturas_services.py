from models.detalles_facturas_model import DetalleFacturaModel

class DetalleFacturaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return DetalleFacturaModel.listar_todos()
    
    def listar_por_factura(self, id_factura):
        return DetalleFacturaModel.listar_por_factura(id_factura)
    
    def crear(self, id_factura, id_servicio, subtotal):
        return DetalleFacturaModel.crear(id_factura, id_servicio, subtotal)
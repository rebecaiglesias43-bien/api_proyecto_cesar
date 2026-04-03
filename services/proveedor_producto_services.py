from models.proveedor_producto_model import ProveedorProductoModel

class ProveedorProductoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return ProveedorProductoModel.listar_todos()
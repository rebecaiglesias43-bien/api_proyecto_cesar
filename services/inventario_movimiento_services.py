from models.inventario_movimiento_model import InventarioMovimientoModel

class InventarioMovimientoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return InventarioMovimientoModel.listar_todos()
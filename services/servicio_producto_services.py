from models.servicio_producto_model import ServicioProductoModel

class ServicioProductoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return ServicioProductoModel.listar_todos()
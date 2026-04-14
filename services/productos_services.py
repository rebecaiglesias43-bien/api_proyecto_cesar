from models.productos_model import ProductoModel

class ProductoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return ProductoModel.listar_todos()
    
    def obtener_por_id(self, id_producto):
        return ProductoModel.obtener_por_id(id_producto)
    
    def crear(self, nombre, precio, stock, estado):
        return ProductoModel.crear(nombre, precio, stock, estado)
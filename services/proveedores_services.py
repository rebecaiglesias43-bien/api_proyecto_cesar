from models.proveedores_model import ProveedorModel

class ProveedorService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return ProveedorModel.listar_todos()
    
    def obtener_por_id(self, id_proveedor):
        return ProveedorModel.obtener_por_id(id_proveedor)
    
    def crear(self, nombre, telefono, email, direccion):
        return ProveedorModel.crear(nombre, telefono, email, direccion)
    
    def actualizar(self, id_proveedor, nombre, telefono, email, direccion):
        return ProveedorModel.actualizar(id_proveedor, nombre, telefono, email, direccion)
    
    def eliminar(self, id_proveedor):
        return ProveedorModel.eliminar(id_proveedor)
from models.servicios_productos_model import ServicioProductoModel

class ServicioProductoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return ServicioProductoModel.listar_todos()

    def obtener_por_id(self, id_relacion):
        return ServicioProductoModel.obtener_por_id(id_relacion)

    def actualizar(self, id_relacion, id_servicio, id_producto, cantidad):
        return ServicioProductoModel.actualizar(id_relacion, id_servicio, id_producto, cantidad)

    def eliminar(self, id_relacion):
        return ServicioProductoModel.eliminar(id_relacion)

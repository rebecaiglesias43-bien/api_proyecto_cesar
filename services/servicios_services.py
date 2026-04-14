from models.servicios_model import ServicioModel

class ServicioService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return ServicioModel.listar_todos()
    
    def obtener_por_id(self, id_servicio):
        return ServicioModel.obtener_por_id(id_servicio)
    
    def crear(self, nombre, descripcion, precio, duracion):
        return ServicioModel.crear(nombre, descripcion, precio, duracion)
    
    def actualizar(self, id_servicio, nombre, descripcion, precio, duracion):
        return ServicioModel.actualizar(id_servicio, nombre, descripcion, precio, duracion)
    
    def eliminar(self, id_servicio):
        return ServicioModel.eliminar(id_servicio)
from models.empleados_model import EmpleadoModel

class EmpleadoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return EmpleadoModel.listar_todos()
    
    def obtener_por_id(self, id_empleado):
        return EmpleadoModel.obtener_por_id(id_empleado)
    
    def crear(self, id_usuario, nombre, apellido, telefono, cargo, especialidad):
        return EmpleadoModel.crear(id_usuario, nombre, apellido, telefono, cargo, especialidad)
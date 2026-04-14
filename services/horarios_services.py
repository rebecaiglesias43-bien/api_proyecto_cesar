from models.horarios_model import HorarioModel

class HorarioService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return HorarioModel.listar_todos()
    
    def listar_por_empleado(self, id_empleado):
        return HorarioModel.listar_por_empleado(id_empleado)
    
    def crear(self, id_empleado, dia_semana, hora_inicio, hora_fin):
        return HorarioModel.crear(id_empleado, dia_semana, hora_inicio, hora_fin)
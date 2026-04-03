from models.detalle_cita_model import DetalleCitaModel

class DetalleCitaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return DetalleCitaModel.listar_todos()
    
    def listar_por_cita(self, id_cita):
        return DetalleCitaModel.listar_por_cita(id_cita)
    
    def crear(self, id_cita, id_servicio, precio):
        return DetalleCitaModel.crear(id_cita, id_servicio, precio)
from models.detalles_citas_model import DetalleCitaModel

class DetalleCitaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return DetalleCitaModel.listar_todos()
    
    def listar_por_cita(self, id_cita):
        return DetalleCitaModel.listar_por_cita(id_cita)

    def obtener_por_id(self, id_detalle):
        return DetalleCitaModel.obtener_por_id(id_detalle)

    def crear(self, id_cita, id_servicio, precio):
        return DetalleCitaModel.crear(id_cita, id_servicio, precio)

    def actualizar(self, id_detalle, id_cita, id_servicio, precio):
        return DetalleCitaModel.actualizar(id_detalle, id_cita, id_servicio, precio)

    def eliminar(self, id_detalle):
        return DetalleCitaModel.eliminar(id_detalle)

class DetalleCitaModel:
    def __init__(self, id_detallecita, id_cita, id_servicio, precio_servicio):
        self.id_detallecita = id_detallecita
        self.id_cita = id_cita
        self.id_servicio = id_servicio
        self.precio_servicio = precio_servicio
    
    def to_dict(self):
        return {
            'id_detallecita': self.id_detallecita,
            'id_cita': self.id_cita,
            'id_servicio': self.id_servicio,
            'precio_servicio': float(self.precio_servicio) if self.precio_servicio else None
        }
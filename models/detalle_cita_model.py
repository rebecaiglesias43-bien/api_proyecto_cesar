class DetalleCitaModel:
    def __init__(self, id_detallecitaPK, id_citaFK, id_servicioFK, precio_servicio):
        self.id_detallecitaPK = id_detallecitaPK
        self.id_citaFK = id_citaFK
        self.id_servicioFK = id_servicioFK
        self.precio_servicio = precio_servicio
    
    def to_dict(self):
        return {
            'id_detallecitaPK': self.id_detallecitaPK,
            'id_citaFK': self.id_citaFK,
            'id_servicioFK': self.id_servicioFK,
            'precio_servicio': float(self.precio_servicio) if self.precio_servicio else None
        }
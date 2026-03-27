class ServicioModel:
    def __init__(self, id_servicio, nombre_servicio, descripcion, precio, duracion_aprox):
        self.id_servicio = id_servicio
        self.nombre_servicio = nombre_servicio
        self.descripcion = descripcion
        self.precio = precio
        self.duracion_aprox = duracion_aprox
    
    def to_dict(self):
        return {
            'id_servicio': self.id_servicio,
            'nombre_servicio': self.nombre_servicio,
            'descripcion': self.descripcion,
            'precio': float(self.precio) if self.precio else None,
            'duracion_aprox': self.duracion_aprox
        }

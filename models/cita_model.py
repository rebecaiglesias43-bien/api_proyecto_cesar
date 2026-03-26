class CitaModel:
    def __init__(self, id_citaPK, fecha, hora, estado, id_clienteFK, id_empleadoFK):
        self.id_citaPK = id_citaPK
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.id_clienteFK = id_clienteFK
        self.id_empleadoFK = id_empleadoFK
    
    def to_dict(self):
        return {
            'id_citaPK': self.id_citaPK,
            'fecha': str(self.fecha) if self.fecha else None,
            'hora': str(self.hora) if self.hora else None,
            'estado': self.estado,
            'id_clienteFK': self.id_clienteFK,
            'id_empleadoFK': self.id_empleadoFK
        }
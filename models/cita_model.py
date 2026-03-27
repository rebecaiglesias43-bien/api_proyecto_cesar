class CitaModel:
    def __init__(self, id_cita, id_cliente, id_empleado, fecha, hora, estado):
        self.id_cita = id_cita
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
    
    def to_dict(self):
        return {
            'id_cita': self.id_cita,
            'id_cliente': self.id_cliente,
            'id_empleado': self.id_empleado,
            'fecha': str(self.fecha) if self.fecha else None,
            'hora': str(self.hora) if self.hora else None,
            'estado': self.estado
        }
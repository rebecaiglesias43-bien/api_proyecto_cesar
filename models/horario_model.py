class HorarioModel:
    def __init__(self, id_horario, id_empleado, dia_semana, hora_inicio, hora_fin):
        self.id_horario = id_horario
        self.id_empleado = id_empleado
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def to_dict(self):
        return {
            'id_horario': self.id_horario,
            'id_empleado': self.id_empleado,
            'dia_semana': self.dia_semana,
            'hora_inicio': str(self.hora_inicio) if self.hora_inicio else None,
            'hora_fin': str(self.hora_fin) if self.hora_fin else None
        }

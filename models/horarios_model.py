from flask import current_app

class HorarioModel:
    def __init__(self, id_horario=None, id_empleado=None, dia_semana=None, hora_inicio=None, hora_fin=None):
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
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT hor_id, hor_empleado_id, hor_dia_semana, hor_hora_inicio, hor_hora_fin FROM horarios")
        horarios = cursor.fetchall()
        cursor.close()
        resultado = []
        for h in horarios:
            resultado.append(HorarioModel(h[0], h[1], h[2], h[3], h[4]).to_dict())
        return resultado
    
    @staticmethod
    def listar_por_empleado(id_empleado):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT hor_id, hor_empleado_id, hor_dia_semana, hor_hora_inicio, hor_hora_fin FROM horarios WHERE hor_empleado_id = %s", (id_empleado,))
        horarios = cursor.fetchall()
        cursor.close()
        resultado = []
        for h in horarios:
            resultado.append(HorarioModel(h[0], h[1], h[2], h[3], h[4]).to_dict())
        return resultado
    
    @staticmethod
    def crear(id_empleado, dia_semana, hora_inicio, hora_fin):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO horarios (hor_empleado_id, hor_dia_semana, hor_hora_inicio, hor_hora_fin) VALUES (%s, %s, %s, %s)", (id_empleado, dia_semana, hora_inicio, hora_fin))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT hor_id, hor_empleado_id, hor_dia_semana, hor_hora_inicio, hor_hora_fin FROM horarios WHERE hor_id = %s", (id_generado,))
        h = cursor.fetchone()
        cursor.close()
        if h:
            return HorarioModel(h[0], h[1], h[2], h[3], h[4]).to_dict()
        return None
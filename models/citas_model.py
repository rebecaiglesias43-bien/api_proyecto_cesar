from flask import current_app

class CitaModel:
    def __init__(self, id_cita=None, id_cliente=None, id_empleado=None, fecha=None, hora=None, estado=None):
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
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT cit_id, cit_cliente_id, cit_empleado_id, cit_fecha, cit_hora, cit_estado FROM citas")
        citas = cursor.fetchall()
        cursor.close()
        resultado = []
        for c in citas:
            resultado.append(CitaModel(c[0], c[1], c[2], c[3], c[4], c[5]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_cita):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT cit_id, cit_cliente_id, cit_empleado_id, cit_fecha, cit_hora, cit_estado FROM citas WHERE cit_id = %s", (id_cita,))
        c = cursor.fetchone()
        cursor.close()
        if c:
            return CitaModel(c[0], c[1], c[2], c[3], c[4], c[5]).to_dict()
        return None
    
    @staticmethod
    def crear(id_cliente, id_empleado, fecha, hora, estado):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO citas (cit_cliente_id, cit_empleado_id, cit_fecha, cit_hora, cit_estado) VALUES (%s, %s, %s, %s, %s)", (id_cliente, id_empleado, fecha, hora, estado))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return CitaModel.obtener_por_id(id_generado)

    @staticmethod
    def actualizar(id_cita, id_cliente, id_empleado, fecha, hora, estado):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE citas SET cit_cliente_id = %s, cit_empleado_id = %s, cit_fecha = %s, cit_hora = %s, cit_estado = %s WHERE cit_id = %s",
            (id_cliente, id_empleado, fecha, hora, estado, id_cita)
        )
        current_app.mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        if filas == 0:
            return None
        return CitaModel.obtener_por_id(id_cita)

    @staticmethod
    def eliminar(id_cita):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM citas WHERE cit_id = %s", (id_cita,))
        current_app.mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        return filas > 0

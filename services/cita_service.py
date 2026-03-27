from models.cita_model import CitaModel

class CitaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todas(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_cita, id_cliente, id_empleado, fecha, hora, estado FROM cita")
        citas = cursor.fetchall()
        cursor.close()
        resultado = []
        for cita in citas:
            resultado.append(CitaModel(cita[0], cita[1], cita[2], cita[3], cita[4], cita[5]).to_dict())
        return resultado
    
    def obtener_por_id(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_cita, id_cliente, id_empleado, fecha, hora, estado FROM cita WHERE id_cita = %s", (id_cita,))
        cita = cursor.fetchone()
        cursor.close()
        if cita:
            return CitaModel(cita[0], cita[1], cita[2], cita[3], cita[4], cita[5]).to_dict()
        return None
    
    def crear(self, id_cliente, id_empleado, fecha, hora, estado):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO cita (id_cliente, id_empleado, fecha, hora, estado) VALUES (%s, %s, %s, %s, %s)",
            (id_cliente, id_empleado, fecha, hora, estado)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
    
    def actualizar(self, id_cita, id_cliente=None, id_empleado=None, fecha=None, hora=None, estado=None):
        cursor = self.mysql.connection.cursor()
        cita_actual = self.obtener_por_id(id_cita)
        if not cita_actual:
            cursor.close()
            return None
        
        nuevo_cliente = id_cliente if id_cliente is not None else cita_actual['id_cliente']
        nuevo_empleado = id_empleado if id_empleado is not None else cita_actual['id_empleado']
        nueva_fecha = fecha if fecha is not None else cita_actual['fecha']
        nueva_hora = hora if hora is not None else cita_actual['hora']
        nuevo_estado = estado if estado is not None else cita_actual['estado']
        
        cursor.execute(
            "UPDATE cita SET id_cliente=%s, id_empleado=%s, fecha=%s, hora=%s, estado=%s WHERE id_cita=%s",
            (nuevo_cliente, nuevo_empleado, nueva_fecha, nueva_hora, nuevo_estado, id_cita)
        )
        self.mysql.connection.commit()
        cursor.close()
        return self.obtener_por_id(id_cita)
    
    def eliminar(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("DELETE FROM cita WHERE id_cita = %s", (id_cita,))
        self.mysql.connection.commit()
        afectadas = cursor.rowcount
        cursor.close()
        return afectadas > 0
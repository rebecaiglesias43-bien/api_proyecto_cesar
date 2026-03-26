from models.cita_model import CitaModel

class CitaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todas(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM cita")
        citas = cursor.fetchall()
        cursor.close()
        
        resultado = []
        for cita in citas:
            resultado.append(CitaModel(
                cita[0], cita[1], cita[2], cita[3], cita[4], cita[5]
            ).to_dict())
        return resultado
    
    def obtener_por_id(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM cita WHERE id_citaPK = %s", (id_cita,))
        cita = cursor.fetchone()
        cursor.close()
        
        if cita:
            return CitaModel(cita[0], cita[1], cita[2], cita[3], cita[4], cita[5]).to_dict()
        return None
    
    def crear(self, fecha, hora, estado, id_clienteFK, id_empleadoFK):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO cita (fecha, hora, estado, id_clienteFK, id_empleadoFK) VALUES (%s, %s, %s, %s, %s)",
            (fecha, hora, estado, id_clienteFK, id_empleadoFK)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
    
    def actualizar(self, id_cita, fecha=None, hora=None, estado=None, id_clienteFK=None, id_empleadoFK=None):
        cursor = self.mysql.connection.cursor()
        cita_actual = self.obtener_por_id(id_cita)
        if not cita_actual:
            cursor.close()
            return None
        
        # Actualizar solo los campos proporcionados
        nueva_fecha = fecha if fecha is not None else cita_actual['fecha']
        nueva_hora = hora if hora is not None else cita_actual['hora']
        nuevo_estado = estado if estado is not None else cita_actual['estado']
        nuevo_cliente = id_clienteFK if id_clienteFK is not None else cita_actual['id_clienteFK']
        nuevo_empleado = id_empleadoFK if id_empleadoFK is not None else cita_actual['id_empleadoFK']
        
        cursor.execute(
            "UPDATE cita SET fecha=%s, hora=%s, estado=%s, id_clienteFK=%s, id_empleadoFK=%s WHERE id_citaPK=%s",
            (nueva_fecha, nueva_hora, nuevo_estado, nuevo_cliente, nuevo_empleado, id_cita)
        )
        self.mysql.connection.commit()
        cursor.close()
        return self.obtener_por_id(id_cita)
    
    def eliminar(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("DELETE FROM cita WHERE id_citaPK = %s", (id_cita,))
        self.mysql.connection.commit()
        afectadas = cursor.rowcount
        cursor.close()
        return afectadas > 0
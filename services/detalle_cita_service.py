from models.detalle_cita_model import DetalleCitaModel

class DetalleCitaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_detallecita, id_cita, id_servicio, precio_servicio FROM detalle_cita")
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for detalle in detalles:
            resultado.append(DetalleCitaModel(detalle[0], detalle[1], detalle[2], detalle[3]).to_dict())
        return resultado
    
    def listar_por_cita(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_detallecita, id_cita, id_servicio, precio_servicio FROM detalle_cita WHERE id_cita = %s", (id_cita,))
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for detalle in detalles:
            resultado.append(DetalleCitaModel(detalle[0], detalle[1], detalle[2], detalle[3]).to_dict())
        return resultado
    
    def crear(self, id_cita, id_servicio, precio_servicio):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO detalle_cita (id_cita, id_servicio, precio_servicio) VALUES (%s, %s, %s)",
            (id_cita, id_servicio, precio_servicio)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_detallecita, id_cita, id_servicio, precio_servicio FROM detalle_cita WHERE id_detallecita = %s", (id_generado,))
        detalle = cursor.fetchone()
        cursor.close()
        
        if detalle:
            return DetalleCitaModel(detalle[0], detalle[1], detalle[2], detalle[3]).to_dict()
        return None
    
    def eliminar_por_cita(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("DELETE FROM detalle_cita WHERE id_cita = %s", (id_cita,))
        self.mysql.connection.commit()
        afectadas = cursor.rowcount
        cursor.close()
        return afectadas
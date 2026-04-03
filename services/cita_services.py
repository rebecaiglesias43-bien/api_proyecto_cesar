from models.cita_model import CitaModel

class CitaService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todas(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT cit_id, cit_cliente_id, cit_empleado_id, cit_fecha, cit_hora, cit_estado FROM citas")
        citas = cursor.fetchall()
        cursor.close()
        resultado = []
        for c in citas:
            resultado.append(CitaModel(c[0], c[1], c[2], c[3], c[4], c[5]).to_dict())
        return resultado
    
    def obtener_por_id(self, id_cita):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT cit_id, cit_cliente_id, cit_empleado_id, cit_fecha, cit_hora, cit_estado FROM citas WHERE cit_id = %s", (id_cita,))
        c = cursor.fetchone()
        cursor.close()
        if c:
            return CitaModel(c[0], c[1], c[2], c[3], c[4], c[5]).to_dict()
        return None
    
    def crear(self, id_cliente, id_empleado, fecha, hora, estado):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO citas (cit_cliente_id, cit_empleado_id, cit_fecha, cit_hora, cit_estado) VALUES (%s, %s, %s, %s, %s)",
            (id_cliente, id_empleado, fecha, hora, estado)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
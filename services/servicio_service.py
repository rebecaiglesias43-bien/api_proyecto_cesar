from models.servicio_model import ServicioModel

class ServicioService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_servicio, nombre_servicio, descripcion, precio, duracion_aprox FROM servicio")
        servicios = cursor.fetchall()
        cursor.close()
        resultado = []
        for s in servicios:
            resultado.append(ServicioModel(s[0], s[1], s[2], s[3], s[4]).to_dict())
        return resultado
    
    def obtener_por_id(self, id_servicio):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_servicio, nombre_servicio, descripcion, precio, duracion_aprox FROM servicio WHERE id_servicio = %s", (id_servicio,))
        s = cursor.fetchone()
        cursor.close()
        if s:
            return ServicioModel(s[0], s[1], s[2], s[3], s[4]).to_dict()
        return None
    
    def crear(self, nombre_servicio, descripcion, precio, duracion_aprox):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO servicio (nombre_servicio, descripcion, precio, duracion_aprox) VALUES (%s, %s, %s, %s)",
            (nombre_servicio, descripcion, precio, duracion_aprox)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
    
    def actualizar(self, id_servicio, nombre_servicio=None, descripcion=None, precio=None, duracion_aprox=None):
        cursor = self.mysql.connection.cursor()
        actual = self.obtener_por_id(id_servicio)
        if not actual:
            cursor.close()
            return None
        
        n_nombre = nombre_servicio if nombre_servicio is not None else actual['nombre_servicio']
        n_desc = descripcion if descripcion is not None else actual['descripcion']
        n_precio = precio if precio is not None else actual['precio']
        n_duracion = duracion_aprox if duracion_aprox is not None else actual['duracion_aprox']
        
        cursor.execute(
            "UPDATE servicio SET nombre_servicio=%s, descripcion=%s, precio=%s, duracion_aprox=%s WHERE id_servicio=%s",
            (n_nombre, n_desc, n_precio, n_duracion, id_servicio)
        )
        self.mysql.connection.commit()
        cursor.close()
        return self.obtener_por_id(id_servicio)
    
    def eliminar(self, id_servicio):
        cursor = self.mysql.connection.cursor()
        cursor.execute("DELETE FROM servicio WHERE id_servicio = %s", (id_servicio,))
        self.mysql.connection.commit()
        afectadas = cursor.rowcount
        cursor.close()
        return afectadas > 0

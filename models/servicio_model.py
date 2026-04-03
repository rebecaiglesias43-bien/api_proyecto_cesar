from flask import current_app

class ServicioModel:
    def __init__(self, id_servicio=None, nombre=None, descripcion=None, precio=None, duracion=None):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.duracion = duracion
    
    def to_dict(self):
        return {
            'id_servicio': self.id_servicio,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': float(self.precio) if self.precio else None,
            'duracion': self.duracion
        }
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT ser_id, ser_nombre, ser_descripcion, ser_precio, ser_duracion FROM servicios")
        servicios = cursor.fetchall()
        cursor.close()
        resultado = []
        for s in servicios:
            resultado.append(ServicioModel(s[0], s[1], s[2], s[3], s[4]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_servicio):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT ser_id, ser_nombre, ser_descripcion, ser_precio, ser_duracion FROM servicios WHERE ser_id = %s", (id_servicio,))
        s = cursor.fetchone()
        cursor.close()
        if s:
            return ServicioModel(s[0], s[1], s[2], s[3], s[4]).to_dict()
        return None
    
    @staticmethod
    def crear(nombre, descripcion, precio, duracion):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO servicios (ser_nombre, ser_descripcion, ser_precio, ser_duracion) VALUES (%s, %s, %s, %s)", (nombre, descripcion, precio, duracion))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return ServicioModel.obtener_por_id(id_generado)
from flask import current_app

class DetalleCitaModel:
    def __init__(self, id_detalle=None, id_cita=None, id_servicio=None, precio=None):
        self.id_detalle = id_detalle
        self.id_cita = id_cita
        self.id_servicio = id_servicio
        self.precio = precio
    
    def to_dict(self):
        return {
            'id_detalle': self.id_detalle,
            'id_cita': self.id_cita,
            'id_servicio': self.id_servicio,
            'precio': float(self.precio) if self.precio else None
        }
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dci_id, dci_cita_id, dci_servicio_id, dci_precio FROM detalle_citas")
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in detalles:
            resultado.append(DetalleCitaModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
    
    @staticmethod
    def listar_por_cita(id_cita):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dci_id, dci_cita_id, dci_servicio_id, dci_precio FROM detalle_citas WHERE dci_cita_id = %s", (id_cita,))
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in detalles:
            resultado.append(DetalleCitaModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
    
    @staticmethod
    def crear(id_cita, id_servicio, precio):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO detalle_citas (dci_cita_id, dci_servicio_id, dci_precio) VALUES (%s, %s, %s)", (id_cita, id_servicio, precio))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dci_id, dci_cita_id, dci_servicio_id, dci_precio FROM detalle_citas WHERE dci_id = %s", (id_generado,))
        d = cursor.fetchone()
        cursor.close()
        if d:
            return DetalleCitaModel(d[0], d[1], d[2], d[3]).to_dict()
        return None

    @staticmethod
    def obtener_por_id(id_detalle):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dci_id, dci_cita_id, dci_servicio_id, dci_precio FROM detalle_citas WHERE dci_id = %s", (id_detalle,))
        d = cursor.fetchone()
        cursor.close()
        if d:
            return DetalleCitaModel(d[0], d[1], d[2], d[3]).to_dict()
        return None

    @staticmethod
    def actualizar(id_detalle, id_cita, id_servicio, precio):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE detalle_citas SET dci_cita_id = %s, dci_servicio_id = %s, dci_precio = %s WHERE dci_id = %s",
            (id_cita, id_servicio, precio, id_detalle)
        )
        current_app.mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        if filas == 0:
            return None
        return DetalleCitaModel.obtener_por_id(id_detalle)

    @staticmethod
    def eliminar(id_detalle):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM detalle_citas WHERE dci_id = %s", (id_detalle,))
        current_app.mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        return filas > 0

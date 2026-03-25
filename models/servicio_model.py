class Servicio:

    # metodo inicializador
    def __init__(self, id, nombre_servicio, descripcion, precio, duracion_aprox):
        self.id_servicio = id
        self.nombre_servicio = nombre_servicio
        self.descripcion = descripcion
        self.precio = precio
        self.duracion_aprox = duracion_aprox

    # metodo convertir objeto a diccionario
    def toDic(self):
        return {
            "id_servicio": self.id_servicio,
            "nombre_servicio": self.nombre_servicio,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "duracion_aprox": self.duracion_aprox
        }
class Cliente:

    # metodo inicializador
    def __init__(self, id, nombre, apellido, telefono, direccion, id_usuarioFK):
        self.id_cliente = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.id_usuarioFK = id_usuarioFK

    # metodo convertir objeto a diccionario
    def toDic(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "id_usuarioFK": self.id_usuarioFK
        }

class Empleado:

    # metodo inicializador
    def __init__(self, id, nombre, apellido, telefono, especialidad, cargo, id_usuarioFK):
        self.id_empleado = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.especialidad = especialidad
        self.cargo = cargo
        self.id_usuarioFK = id_usuarioFK

    # metodo convertir objeto a diccionario
    def toDic(self):
        return {
            "id_empleado": self.id_empleado,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "especialidad": self.especialidad,
            "cargo": self.cargo,
            "id_usuarioFK": self.id_usuarioFK
        }
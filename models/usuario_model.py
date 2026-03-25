class Usuario:

    # metodo inicializador
    def __init__(self, id, nombre_usuario, apellido, correo, telefono, direccion, contrasena, rol, estado):
        self.id_usuario = id
        self.nombre_usuario = nombre_usuario
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.contrasena = contrasena
        self.rol = rol
        self.estado = estado

    # metodo convertir objeto a diccionario
    def toDic(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "apellido": self.apellido,
            "correo": self.correo,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "contrasena": self.contrasena,
            "rol": self.rol,
            "estado": self.estado
        }
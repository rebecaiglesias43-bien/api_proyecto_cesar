class UsuarioModel:
    def __init__(self, id_usuario=None, username=None, password=None, email=None, rol=None, estado=None):
        self.id_usuario = id_usuario
        self.username = username
        self.password = password
        self.email = email
        self.rol = rol
        self.estado = estado
    
    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'username': self.username,
            'email': self.email,
            'rol': self.rol,
            'estado': self.estado
        }
    
    @staticmethod
    def listar_todos(mysql):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT usu_id, usu_username, usu_password, usu_email, usu_rol, usu_estado FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        resultado = []
        for u in usuarios:
            resultado.append(UsuarioModel(u[0], u[1], u[2], u[3], u[4], u[5]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(mysql, id_usuario):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT usu_id, usu_username, usu_password, usu_email, usu_rol, usu_estado FROM usuarios WHERE usu_id = %s", (id_usuario,))
        u = cursor.fetchone()
        cursor.close()
        if u:
            return UsuarioModel(u[0], u[1], u[2], u[3], u[4], u[5]).to_dict()
        return None
    
    @staticmethod
    def crear(mysql, username, password, email, rol, estado):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios (usu_username, usu_password, usu_email, usu_rol, usu_estado) VALUES (%s, %s, %s, %s, %s)", (username, password, email, rol, estado))
        mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return UsuarioModel.obtener_por_id(mysql, id_generado)

    @staticmethod
    def autenticar(mysql, username, password):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT usu_id, usu_username, usu_password, usu_email, usu_rol, usu_estado "
            "FROM usuarios WHERE usu_username = %s AND usu_password = %s AND usu_estado = %s",
            (username, password, 'activo')
        )
        u = cursor.fetchone()
        cursor.close()
        if u:
            return UsuarioModel(u[0], u[1], u[2], u[3], u[4], u[5]).to_dict()
        return None

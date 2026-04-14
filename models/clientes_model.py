from flask import current_app

class Cliente:
    def __init__(self, id_cliente=None, id_usuario=None, nombre=None, apellido=None, telefono=None, direccion=None):
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
    
    def to_dict(self):
        return {
            'id_cliente': self.id_cliente,
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'direccion': self.direccion
        }
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT cli_id, cli_usuario_id, cli_nombre, cli_apellido, cli_telefono, cli_direccion FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        resultado = []
        for c in clientes:
            resultado.append(Cliente(c[0], c[1], c[2], c[3], c[4], c[5]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_cliente):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT cli_id, cli_usuario_id, cli_nombre, cli_apellido, cli_telefono, cli_direccion FROM clientes WHERE cli_id = %s", (id_cliente,))
        c = cursor.fetchone()
        cursor.close()
        if c:
            return Cliente(c[0], c[1], c[2], c[3], c[4], c[5]).to_dict()
        return None
    
    @staticmethod
    def crear(id_usuario, nombre, apellido, telefono, direccion):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO clientes (cli_usuario_id, cli_nombre, cli_apellido, cli_telefono, cli_direccion) VALUES (%s, %s, %s, %s, %s)", (id_usuario, nombre, apellido, telefono, direccion))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return Cliente.obtener_por_id(id_generado)
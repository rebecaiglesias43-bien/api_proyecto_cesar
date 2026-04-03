from models.cliente_model import Cliente

class ClienteService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT cli_id, cli_usuario_id, cli_nombre, cli_apellido, cli_telefono, cli_direccion FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        resultado = []
        for c in clientes:
            resultado.append(Cliente(c[0], c[1], c[2], c[3], c[4], c[5]).to_dict())
        return resultado
    
    def obtener_por_id(self, id_cliente):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT cli_id, cli_usuario_id, cli_nombre, cli_apellido, cli_telefono, cli_direccion FROM clientes WHERE cli_id = %s", (id_cliente,))
        c = cursor.fetchone()
        cursor.close()
        if c:
            return Cliente(c[0], c[1], c[2], c[3], c[4], c[5]).to_dict()
        return None
    
    def crear(self, id_usuario, nombre, apellido, telefono, direccion):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO clientes (cli_usuario_id, cli_nombre, cli_apellido, cli_telefono, cli_direccion) VALUES (%s, %s, %s, %s, %s)",
            (id_usuario, nombre, apellido, telefono, direccion)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
from models.usuarios_model import UsuarioModel

class UsuarioService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return UsuarioModel.listar_todos(self.mysql)
    
    def obtener_por_id(self, id_usuario):
        return UsuarioModel.obtener_por_id(self.mysql, id_usuario)
    
    def crear(self, username, password, email, rol, estado):
        return UsuarioModel.crear(self.mysql, username, password, email, rol, estado)

    def autenticar(self, username, password):
        return UsuarioModel.autenticar(self.mysql, username, password)

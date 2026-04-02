from models.usuario_model import UsuarioModel

class UsuarioService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        return UsuarioModel.listar_todos()
    
    def obtener_por_id(self, id_usuario):
        return UsuarioModel.obtener_por_id(id_usuario)
    
    def crear(self, username, password, email, rol, estado):
        return UsuarioModel.crear(username, password, email, rol, estado)
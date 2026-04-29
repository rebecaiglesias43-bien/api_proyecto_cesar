from models.proveedores_model import ProveedorModel


class ProveedorService:
    def __init__(self, mysql):
        self.mysql = mysql

    def listar_todos(self, page, per_page):
        return ProveedorModel.listar_todos(self.mysql, page, per_page)

    def obtener_por_id(self, id_proveedor):
        return ProveedorModel.obtener_por_id(self.mysql, id_proveedor)

    def crear(self, nombre, telefono, email, direccion):
        return ProveedorModel.crear(self.mysql, nombre, telefono, email, direccion)

    def actualizar(self, id_proveedor, nombre, telefono, email, direccion):
        return ProveedorModel.actualizar(
            self.mysql,
            id_proveedor,
            nombre,
            telefono,
            email,
            direccion
        )

    def eliminar(self, id_proveedor):
        if not ProveedorModel.obtener_por_id(self.mysql, id_proveedor):
            return False
        if ProveedorModel.tiene_productos_asociados(self.mysql, id_proveedor):
            raise ValueError('No se puede eliminar el proveedor porque tiene productos asociados')
        return ProveedorModel.eliminar(self.mysql, id_proveedor)

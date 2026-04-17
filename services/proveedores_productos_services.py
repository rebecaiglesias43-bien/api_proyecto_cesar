from models.proveedores_productos_model import ProveedorProductoModel


class ProveedorProductoService:
    def __init__(self, mysql):
        self.mysql = mysql

    def listar_todos(self):
        return ProveedorProductoModel.listar_todos(self.mysql)

    def obtener_por_id(self, id_relacion):
        return ProveedorProductoModel.obtener_por_id(self.mysql, id_relacion)

    def crear(self, id_proveedor, id_producto, precio):
        return ProveedorProductoModel.crear(self.mysql, id_proveedor, id_producto, precio)

    def actualizar(self, id_relacion, id_proveedor, id_producto, precio):
        return ProveedorProductoModel.actualizar(
            self.mysql,
            id_relacion,
            id_proveedor,
            id_producto,
            precio
        )

    def eliminar(self, id_relacion):
        return ProveedorProductoModel.eliminar(self.mysql, id_relacion)

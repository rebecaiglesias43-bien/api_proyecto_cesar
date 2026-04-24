from models.proveedores_productos_model import ProveedorProductoModel


class ProveedorProductoService:
    def __init__(self, mysql):
        self.mysql = mysql

    def listar_todos(self):
        return ProveedorProductoModel.listar_todos(self.mysql)

    def obtener_por_id(self, id_relacion):
        return ProveedorProductoModel.obtener_por_id(self.mysql, id_relacion)

    def crear(self, id_proveedor, id_producto, precio):
        if not ProveedorProductoModel.proveedor_existe(self.mysql, id_proveedor):
            raise LookupError('El proveedor indicado no existe')
        if not ProveedorProductoModel.producto_existe(self.mysql, id_producto):
            raise LookupError('El producto indicado no existe')
        if ProveedorProductoModel.relacion_duplicada(self.mysql, id_proveedor, id_producto):
            raise ValueError('Ya existe una relacion para el proveedor y producto indicados')
        return ProveedorProductoModel.crear(self.mysql, id_proveedor, id_producto, precio)

    def actualizar(self, id_relacion, id_proveedor, id_producto, precio):
        if not ProveedorProductoModel.obtener_por_id(self.mysql, id_relacion):
            return None
        if not ProveedorProductoModel.proveedor_existe(self.mysql, id_proveedor):
            raise LookupError('El proveedor indicado no existe')
        if not ProveedorProductoModel.producto_existe(self.mysql, id_producto):
            raise LookupError('El producto indicado no existe')
        if ProveedorProductoModel.relacion_duplicada(
            self.mysql,
            id_proveedor,
            id_producto,
            id_relacion
        ):
            raise ValueError('Ya existe una relacion para el proveedor y producto indicados')
        return ProveedorProductoModel.actualizar(
            self.mysql,
            id_relacion,
            id_proveedor,
            id_producto,
            precio
        )

    def eliminar(self, id_relacion):
        return ProveedorProductoModel.eliminar(self.mysql, id_relacion)

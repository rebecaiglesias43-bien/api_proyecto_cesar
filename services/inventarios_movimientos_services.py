from models.inventarios_movimientos_model import InventarioMovimientoModel


class InventarioMovimientoService:
    def __init__(self, mysql):
        self.mysql = mysql

    def listar_todos(self, page, per_page):
        return InventarioMovimientoModel.listar_todos(self.mysql, page, per_page)

    def obtener_por_id(self, id_movimiento):
        return InventarioMovimientoModel.obtener_por_id(self.mysql, id_movimiento)

    def crear(self, id_producto, tipo, cantidad, fecha, motivo):
        return InventarioMovimientoModel.crear(
            self.mysql,
            id_producto,
            tipo,
            cantidad,
            fecha,
            motivo
        )

    def actualizar(self, id_movimiento, id_producto, tipo, cantidad, fecha, motivo):
        return InventarioMovimientoModel.actualizar(
            self.mysql,
            id_movimiento,
            id_producto,
            tipo,
            cantidad,
            fecha,
            motivo
        )

    def eliminar(self, id_movimiento):
        return InventarioMovimientoModel.eliminar(self.mysql, id_movimiento)

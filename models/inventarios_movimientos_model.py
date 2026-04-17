class InventarioMovimientoModel:
    @staticmethod
    def _serialize_row(columns, row):
        item = dict(zip(columns, row))
        if item.get('inm_fecha') is not None:
            item['inm_fecha'] = item['inm_fecha'].isoformat()
        return item

    @staticmethod
    def listar_todos(mysql):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT inm_id, inm_producto_id, inm_tipo, inm_cantidad, inm_fecha, inm_motivo "
            "FROM inventario_movimientos"
        )
        columns = [col[0] for col in cursor.description]
        data = [InventarioMovimientoModel._serialize_row(columns, row) for row in cursor.fetchall()]
        cursor.close()
        return data

    @staticmethod
    def obtener_por_id(mysql, id_movimiento):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT inm_id, inm_producto_id, inm_tipo, inm_cantidad, inm_fecha, inm_motivo "
            "FROM inventario_movimientos WHERE inm_id = %s",
            (id_movimiento,)
        )
        columns = [col[0] for col in cursor.description]
        rows = [InventarioMovimientoModel._serialize_row(columns, row) for row in cursor.fetchall()]
        cursor.close()
        if not rows:
            return None
        return rows[0]

    @staticmethod
    def crear(mysql, id_producto, tipo, cantidad, fecha, motivo):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO inventario_movimientos "
            "(inm_producto_id, inm_tipo, inm_cantidad, inm_fecha, inm_motivo) "
            "VALUES (%s, %s, %s, %s, %s)",
            (id_producto, tipo, cantidad, fecha, motivo)
        )
        mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return InventarioMovimientoModel.obtener_por_id(mysql, id_generado)

    @staticmethod
    def actualizar(mysql, id_movimiento, id_producto, tipo, cantidad, fecha, motivo):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE inventario_movimientos "
            "SET inm_producto_id = %s, inm_tipo = %s, inm_cantidad = %s, inm_fecha = %s, "
            "inm_motivo = %s WHERE inm_id = %s",
            (id_producto, tipo, cantidad, fecha, motivo, id_movimiento)
        )
        mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        if filas == 0:
            return None
        return InventarioMovimientoModel.obtener_por_id(mysql, id_movimiento)

    @staticmethod
    def eliminar(mysql, id_movimiento):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM inventario_movimientos WHERE inm_id = %s", (id_movimiento,))
        mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        return filas > 0

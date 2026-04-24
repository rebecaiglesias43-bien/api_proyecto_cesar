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
    def _delta_stock(tipo, cantidad):
        return cantidad if tipo == 'entrada' else -cantidad

    @staticmethod
    def _obtener_movimiento(cursor, id_movimiento):
        cursor.execute(
            "SELECT inm_id, inm_producto_id, inm_tipo, inm_cantidad "
            "FROM inventario_movimientos WHERE inm_id = %s FOR UPDATE",
            (id_movimiento,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return {
            'inm_id': row[0],
            'inm_producto_id': row[1],
            'inm_tipo': row[2],
            'inm_cantidad': row[3]
        }

    @staticmethod
    def _ajustar_stock(cursor, id_producto, delta):
        cursor.execute(
            "SELECT pro_stock FROM productos WHERE pro_id = %s FOR UPDATE",
            (id_producto,)
        )
        row = cursor.fetchone()
        if not row:
            raise LookupError('El producto indicado no existe')

        stock_actual = row[0] if row[0] is not None else 0
        nuevo_stock = stock_actual + delta
        if nuevo_stock < 0:
            raise ValueError('El movimiento deja el stock del producto en negativo')

        cursor.execute(
            "UPDATE productos SET pro_stock = %s WHERE pro_id = %s",
            (nuevo_stock, id_producto)
        )

    @staticmethod
    def crear(mysql, id_producto, tipo, cantidad, fecha, motivo):
        connection = mysql.connection
        cursor = connection.cursor()
        try:
            delta = InventarioMovimientoModel._delta_stock(tipo, cantidad)
            InventarioMovimientoModel._ajustar_stock(cursor, id_producto, delta)
            cursor.execute(
                "INSERT INTO inventario_movimientos "
                "(inm_producto_id, inm_tipo, inm_cantidad, inm_fecha, inm_motivo) "
                "VALUES (%s, %s, %s, %s, %s)",
                (id_producto, tipo, cantidad, fecha, motivo)
            )
            id_generado = cursor.lastrowid
            connection.commit()
            return InventarioMovimientoModel.obtener_por_id(mysql, id_generado)
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()

    @staticmethod
    def actualizar(mysql, id_movimiento, id_producto, tipo, cantidad, fecha, motivo):
        connection = mysql.connection
        cursor = connection.cursor()
        try:
            movimiento_actual = InventarioMovimientoModel._obtener_movimiento(cursor, id_movimiento)
            if not movimiento_actual:
                return None

            delta_anterior = InventarioMovimientoModel._delta_stock(
                movimiento_actual['inm_tipo'],
                movimiento_actual['inm_cantidad']
            )
            InventarioMovimientoModel._ajustar_stock(
                cursor,
                movimiento_actual['inm_producto_id'],
                -delta_anterior
            )

            delta_nuevo = InventarioMovimientoModel._delta_stock(tipo, cantidad)
            InventarioMovimientoModel._ajustar_stock(cursor, id_producto, delta_nuevo)

            cursor.execute(
                "UPDATE inventario_movimientos "
                "SET inm_producto_id = %s, inm_tipo = %s, inm_cantidad = %s, inm_fecha = %s, "
                "inm_motivo = %s WHERE inm_id = %s",
                (id_producto, tipo, cantidad, fecha, motivo, id_movimiento)
            )
            connection.commit()
            return InventarioMovimientoModel.obtener_por_id(mysql, id_movimiento)
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()

    @staticmethod
    def eliminar(mysql, id_movimiento):
        connection = mysql.connection
        cursor = connection.cursor()
        try:
            movimiento_actual = InventarioMovimientoModel._obtener_movimiento(cursor, id_movimiento)
            if not movimiento_actual:
                return False

            delta_anterior = InventarioMovimientoModel._delta_stock(
                movimiento_actual['inm_tipo'],
                movimiento_actual['inm_cantidad']
            )
            InventarioMovimientoModel._ajustar_stock(
                cursor,
                movimiento_actual['inm_producto_id'],
                -delta_anterior
            )
            cursor.execute("DELETE FROM inventario_movimientos WHERE inm_id = %s", (id_movimiento,))
            connection.commit()
            return cursor.rowcount > 0
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()

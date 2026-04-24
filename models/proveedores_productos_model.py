from decimal import Decimal


class ProveedorProductoModel:
    @staticmethod
    def _serialize_row(columns, row):
        item = dict(zip(columns, row))
        if isinstance(item.get('ppr_precio'), Decimal):
            item['ppr_precio'] = float(item['ppr_precio'])
        return item

    @staticmethod
    def listar_todos(mysql):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT ppr_id, ppr_proveedor_id, ppr_producto_id, ppr_precio FROM proveedores_productos"
        )
        columns = [col[0] for col in cursor.description]
        data = [ProveedorProductoModel._serialize_row(columns, row) for row in cursor.fetchall()]
        cursor.close()
        return data

    @staticmethod
    def obtener_por_id(mysql, id_relacion):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT ppr_id, ppr_proveedor_id, ppr_producto_id, ppr_precio "
            "FROM proveedores_productos WHERE ppr_id = %s",
            (id_relacion,)
        )
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        cursor.close()
        if not rows:
            return None
        return ProveedorProductoModel._serialize_row(columns, rows[0])

    @staticmethod
    def proveedor_existe(mysql, id_proveedor):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1 FROM proveedores WHERE prv_id = %s", (id_proveedor,))
        existe = cursor.fetchone() is not None
        cursor.close()
        return existe

    @staticmethod
    def producto_existe(mysql, id_producto):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1 FROM productos WHERE pro_id = %s", (id_producto,))
        existe = cursor.fetchone() is not None
        cursor.close()
        return existe

    @staticmethod
    def relacion_duplicada(mysql, id_proveedor, id_producto, excluir_id=None):
        cursor = mysql.connection.cursor()
        query = (
            "SELECT 1 FROM proveedores_productos "
            "WHERE ppr_proveedor_id = %s AND ppr_producto_id = %s"
        )
        params = [id_proveedor, id_producto]
        if excluir_id is not None:
            query += " AND ppr_id <> %s"
            params.append(excluir_id)

        cursor.execute(query, tuple(params))
        existe = cursor.fetchone() is not None
        cursor.close()
        return existe

    @staticmethod
    def crear(mysql, id_proveedor, id_producto, precio):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO proveedores_productos (ppr_proveedor_id, ppr_producto_id, ppr_precio) "
            "VALUES (%s, %s, %s)",
            (id_proveedor, id_producto, precio)
        )
        mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return ProveedorProductoModel.obtener_por_id(mysql, id_generado)

    @staticmethod
    def actualizar(mysql, id_relacion, id_proveedor, id_producto, precio):
        if not ProveedorProductoModel.obtener_por_id(mysql, id_relacion):
            return None

        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE proveedores_productos "
            "SET ppr_proveedor_id = %s, ppr_producto_id = %s, ppr_precio = %s "
            "WHERE ppr_id = %s",
            (id_proveedor, id_producto, precio, id_relacion)
        )
        mysql.connection.commit()
        cursor.close()
        return ProveedorProductoModel.obtener_por_id(mysql, id_relacion)

    @staticmethod
    def eliminar(mysql, id_relacion):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM proveedores_productos WHERE ppr_id = %s", (id_relacion,))
        mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        return filas > 0

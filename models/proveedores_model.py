class ProveedorModel:
    @staticmethod
    def listar_todos(mysql, page, per_page):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM proveedores")
        total = cursor.fetchone()[0]
        offset = (page - 1) * per_page
        cursor.execute(
            "SELECT prv_id, prv_nombre, prv_telefono, prv_email, prv_direccion "
            "FROM proveedores ORDER BY prv_id LIMIT %s OFFSET %s",
            (per_page, offset)
        )
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        total_pages = (total + per_page - 1) // per_page if total else 0
        return {
            'data': data,
            'total': total,
            'page': page,
            'per_page': per_page,
            'total_pages': total_pages
        }

    @staticmethod
    def obtener_por_id(mysql, id_proveedor):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT prv_id, prv_nombre, prv_telefono, prv_email, prv_direccion "
            "FROM proveedores WHERE prv_id = %s",
            (id_proveedor,)
        )
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        cursor.close()
        if not rows:
            return None
        return dict(zip(columns, rows[0]))

    @staticmethod
    def crear(mysql, nombre, telefono, email, direccion):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO proveedores (prv_nombre, prv_telefono, prv_email, prv_direccion) "
            "VALUES (%s, %s, %s, %s)",
            (nombre, telefono, email, direccion)
        )
        mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return ProveedorModel.obtener_por_id(mysql, id_generado)

    @staticmethod
    def tiene_productos_asociados(mysql, id_proveedor):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT 1 FROM proveedores_productos WHERE ppr_proveedor_id = %s LIMIT 1",
            (id_proveedor,)
        )
        existe = cursor.fetchone() is not None
        cursor.close()
        return existe

    @staticmethod
    def actualizar(mysql, id_proveedor, nombre, telefono, email, direccion):
        if not ProveedorModel.obtener_por_id(mysql, id_proveedor):
            return None

        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE proveedores "
            "SET prv_nombre = %s, prv_telefono = %s, prv_email = %s, prv_direccion = %s "
            "WHERE prv_id = %s",
            (nombre, telefono, email, direccion, id_proveedor)
        )
        mysql.connection.commit()
        cursor.close()
        return ProveedorModel.obtener_por_id(mysql, id_proveedor)

    @staticmethod
    def eliminar(mysql, id_proveedor):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM proveedores WHERE prv_id = %s", (id_proveedor,))
        mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        return filas > 0

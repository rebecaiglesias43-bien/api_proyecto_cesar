class ProveedorModel:
    @staticmethod
    def listar_todos(mysql):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT prv_id, prv_nombre, prv_telefono, prv_email, prv_direccion FROM proveedores"
        )
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        return data

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
    def actualizar(mysql, id_proveedor, nombre, telefono, email, direccion):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE proveedores "
            "SET prv_nombre = %s, prv_telefono = %s, prv_email = %s, prv_direccion = %s "
            "WHERE prv_id = %s",
            (nombre, telefono, email, direccion, id_proveedor)
        )
        mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        if filas == 0:
            return None
        return ProveedorModel.obtener_por_id(mysql, id_proveedor)

    @staticmethod
    def eliminar(mysql, id_proveedor):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM proveedores WHERE prv_id = %s", (id_proveedor,))
        mysql.connection.commit()
        filas = cursor.rowcount
        cursor.close()
        return filas > 0

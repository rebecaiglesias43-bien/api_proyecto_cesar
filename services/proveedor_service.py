from models.proveedor_model import ProveedorModel

class ProveedorService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_proveedor, nombre_proveedor, telefono, correo, direccion FROM proveedor")
        proveedores = cursor.fetchall()
        cursor.close()
        resultado = []
        for proveedor in proveedores:
            resultado.append(ProveedorModel(proveedor[0], proveedor[1], proveedor[2], proveedor[3], proveedor[4]).to_dict())
        return resultado
    
    def obtener_por_id(self, id_proveedor):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id_proveedor, nombre_proveedor, telefono, correo, direccion FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))
        proveedor = cursor.fetchone()
        cursor.close()
        if proveedor:
            return ProveedorModel(proveedor[0], proveedor[1], proveedor[2], proveedor[3], proveedor[4]).to_dict()
        return None
    
    def crear(self, nombre_proveedor, telefono, correo, direccion):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO proveedor (nombre_proveedor, telefono, correo, direccion) VALUES (%s, %s, %s, %s)",
            (nombre_proveedor, telefono, correo, direccion)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
    
    def actualizar(self, id_proveedor, nombre_proveedor=None, telefono=None, correo=None, direccion=None):
        cursor = self.mysql.connection.cursor()
        proveedor_actual = self.obtener_por_id(id_proveedor)
        if not proveedor_actual:
            cursor.close()
            return None
        
        nuevo_nombre = nombre_proveedor if nombre_proveedor is not None else proveedor_actual['nombre_proveedor']
        nuevo_telefono = telefono if telefono is not None else proveedor_actual['telefono']
        nuevo_correo = correo if correo is not None else proveedor_actual['correo']
        nueva_direccion = direccion if direccion is not None else proveedor_actual['direccion']
        
        cursor.execute(
            "UPDATE proveedor SET nombre_proveedor=%s, telefono=%s, correo=%s, direccion=%s WHERE id_proveedor=%s",
            (nuevo_nombre, nuevo_telefono, nuevo_correo, nueva_direccion, id_proveedor)
        )
        self.mysql.connection.commit()
        cursor.close()
        return self.obtener_por_id(id_proveedor)
    
    def eliminar(self, id_proveedor):
        cursor = self.mysql.connection.cursor()
        cursor.execute("DELETE FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))
        self.mysql.connection.commit()
        afectadas = cursor.rowcount
        cursor.close()
        return afectadas > 0
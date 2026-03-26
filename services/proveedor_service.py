from models.proveedor_model import ProveedorModel

class ProveedorService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def listar_todos(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM proveedor")
        proveedores = cursor.fetchall()
        cursor.close()
        
        resultado = []
        for proveedor in proveedores:
            resultado.append(ProveedorModel(
                proveedor[0], proveedor[1], proveedor[2], proveedor[3]
            ).to_dict())
        return resultado
    
    def obtener_por_id(self, id_proveedor):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))
        proveedor = cursor.fetchone()
        cursor.close()
        
        if proveedor:
            return ProveedorModel(proveedor[0], proveedor[1], proveedor[2], proveedor[3]).to_dict()
        return None
    
    def crear(self, nombre_contacto, empresa, telefono):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO proveedor (nombre_contacto, empresa, telefono) VALUES (%s, %s, %s)",
            (nombre_contacto, empresa, telefono)
        )
        self.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return self.obtener_por_id(id_generado)
    
    def actualizar(self, id_proveedor, nombre_contacto=None, empresa=None, telefono=None):
        cursor = self.mysql.connection.cursor()
        proveedor_actual = self.obtener_por_id(id_proveedor)
        if not proveedor_actual:
            cursor.close()
            return None
        
        nuevo_nombre = nombre_contacto if nombre_contacto is not None else proveedor_actual['nombre_contacto']
        nueva_empresa = empresa if empresa is not None else proveedor_actual['empresa']
        nuevo_telefono = telefono if telefono is not None else proveedor_actual['telefono']
        
        cursor.execute(
            "UPDATE proveedor SET nombre_contacto=%s, empresa=%s, telefono=%s WHERE id_proveedor=%s",
            (nuevo_nombre, nueva_empresa, nuevo_telefono, id_proveedor)
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
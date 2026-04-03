from flask import current_app

class ProveedorModel:
    def __init__(self, id_proveedor=None, nombre=None, telefono=None, email=None, direccion=None):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
    
    def to_dict(self):
        return {
            'id_proveedor': self.id_proveedor,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'email': self.email,
            'direccion': self.direccion
        }
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT prv_id, prv_nombre, prv_telefono, prv_email, prv_direccion FROM proveedores")
        proveedores = cursor.fetchall()
        cursor.close()
        resultado = []
        for p in proveedores:
            resultado.append(ProveedorModel(p[0], p[1], p[2], p[3], p[4]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_proveedor):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT prv_id, prv_nombre, prv_telefono, prv_email, prv_direccion FROM proveedores WHERE prv_id = %s", (id_proveedor,))
        p = cursor.fetchone()
        cursor.close()
        if p:
            return ProveedorModel(p[0], p[1], p[2], p[3], p[4]).to_dict()
        return None
    
    @staticmethod
    def crear(nombre, telefono, email, direccion):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO proveedores (prv_nombre, prv_telefono, prv_email, prv_direccion) VALUES (%s, %s, %s, %s)", (nombre, telefono, email, direccion))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return ProveedorModel.obtener_por_id(id_generado)
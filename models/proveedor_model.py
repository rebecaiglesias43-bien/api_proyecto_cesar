class ProveedorModel:
    def __init__(self, id_proveedor, nombre_proveedor, telefono, correo, direccion):
        self.id_proveedor = id_proveedor
        self.nombre_proveedor = nombre_proveedor
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
    
    def to_dict(self):
        return {
            'id_proveedor': self.id_proveedor,
            'nombre_proveedor': self.nombre_proveedor,
            'telefono': self.telefono,
            'correo': self.correo,
            'direccion': self.direccion
        }
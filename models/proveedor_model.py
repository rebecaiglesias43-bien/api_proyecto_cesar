class ProveedorModel:
    def __init__(self, id_proveedor, nombre_contacto, empresa, telefono):
        self.id_proveedor = id_proveedor
        self.nombre_contacto = nombre_contacto
        self.empresa = empresa
        self.telefono = telefono
    
    def to_dict(self):
        return {
            'id_proveedor': self.id_proveedor,
            'nombre_contacto': self.nombre_contacto,
            'empresa': self.empresa,
            'telefono': self.telefono
        }
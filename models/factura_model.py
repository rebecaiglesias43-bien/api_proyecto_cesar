class FacturaModel:
    def __init__(self, id_factura, id_citaFK, total, fecha_emision):
        self.id_factura = id_factura
        self.id_citaFK = id_citaFK
        self.total = total
        self.fecha_emision = fecha_emision
    
    def to_dict(self):
        return {
            'id_factura': self.id_factura,
            'id_citaFK': self.id_citaFK,
            'total': float(self.total) if self.total else None,
            'fecha_emision': str(self.fecha_emision) if self.fecha_emision else None
        }
class FacturaModel:
    def __init__(self, id_factura, id_cita, fecha, total, estado):
        self.id_factura = id_factura
        self.id_cita = id_cita
        self.fecha = fecha
        self.total = total
        self.estado = estado
    
    def to_dict(self):
        return {
            'id_factura': self.id_factura,
            'id_cita': self.id_cita,
            'fecha': str(self.fecha) if self.fecha else None,
            'total': float(self.total) if self.total else None,
            'estado': self.estado
        }
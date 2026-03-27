class DetalleFacturaModel:
    def __init__(self, id_detalle, id_factura, id_servicio, subtotal):
        self.id_detalle = id_detalle
        self.id_factura = id_factura
        self.id_servicio = id_servicio
        self.subtotal = subtotal
    
    def to_dict(self):
        return {
            'id_detalle': self.id_detalle,
            'id_factura': self.id_factura,
            'id_servicio': self.id_servicio,
            'subtotal': float(self.subtotal) if self.subtotal else None
        }

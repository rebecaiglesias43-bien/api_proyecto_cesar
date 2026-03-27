class PagoModel:
    def __init__(self, id_pago, id_factura, metodo_pago, fecha_pago, monto):
        self.id_pago = id_pago
        self.id_factura = id_factura
        self.metodo_pago = metodo_pago
        self.fecha_pago = fecha_pago
        self.monto = monto
    
    def to_dict(self):
        return {
            'id_pago': self.id_pago,
            'id_factura': self.id_factura,
            'metodo_pago': self.metodo_pago,
            'fecha_pago': str(self.fecha_pago) if self.fecha_pago else None,
            'monto': float(self.monto) if self.monto else None
        }

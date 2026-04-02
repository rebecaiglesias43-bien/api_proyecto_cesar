from .cliente import cliente_bp
from .cita import cita_bp
from .detalle_cita import detalle_cita_bp
from .factura import factura_bp
from .proveedor import proveedor_bp
from .servicio import servicio_bp

def cargarRutas(app):
    app.register_blueprint(cliente_bp, url_prefix='/clientes')        # plural
    app.register_blueprint(cita_bp, url_prefix='/citas')              # plural
    app.register_blueprint(detalle_cita_bp, url_prefix='/detalle-citas')  # plural
    app.register_blueprint(factura_bp, url_prefix='/facturas')        # plural
    app.register_blueprint(proveedor_bp, url_prefix='/proveedores')   # plural
    app.register_blueprint(servicio_bp, url_prefix='/servicios')      # plural
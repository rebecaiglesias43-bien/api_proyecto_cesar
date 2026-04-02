from .cliente import cliente_bp
from .cita import cita_bp
from .detalle_cita import detalle_cita_bp
from .factura import factura_bp
from .proveedor import proveedor_bp

def cargarRutas(app):
    app.register_blueprint(cliente_bp, url_prefix='/cliente')
    app.register_blueprint(cita_bp, url_prefix='/cita')
    app.register_blueprint(detalle_cita_bp, url_prefix='/detalle_cita')
    app.register_blueprint(factura_bp, url_prefix='/factura')
    app.register_blueprint(proveedor_bp, url_prefix='/proveedor')
from .cliente import cliente_bp
from .cita import cita_bp
from .detalle_cita import detalle_cita_bp
from .detalle_factura import detalle_factura_bp  # ← Agregar esta línea
from .factura import factura_bp
from .proveedor import proveedor_bp
from .servicio import servicio_bp
from .pago import pago_bp
from .empleado import empleado_bp
from .horario import horario_bp
from .usuario import usuario_bp
from .producto import producto_bp

def cargarRutas(app):
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(cita_bp, url_prefix='/citas')
    app.register_blueprint(detalle_cita_bp, url_prefix='/detalle-citas')
    app.register_blueprint(detalle_factura_bp, url_prefix='/detalle-facturas')  # ← Agregar esta línea
    app.register_blueprint(factura_bp, url_prefix='/facturas')
    app.register_blueprint(proveedor_bp, url_prefix='/proveedores')
    app.register_blueprint(servicio_bp, url_prefix='/servicios')
    app.register_blueprint(pago_bp, url_prefix='/pagos')
    app.register_blueprint(empleado_bp, url_prefix='/empleados')
    app.register_blueprint(horario_bp, url_prefix='/horarios')
    app.register_blueprint(usuario_bp, url_prefix='/usuarios')
    app.register_blueprint(producto_bp, url_prefix='/productos')
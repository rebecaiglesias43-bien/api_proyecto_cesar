from .clientes import cliente_bp
from .citas import cita_bp
from .detalles_citas import detalle_cita_bp
from .detalles_facturas import detalle_factura_bp
from .facturas import factura_bp
from .proveedores import proveedor_bp
from .servicios import servicio_bp
from .pagos import pago_bp
from .empleados import empleado_bp
from .horarios import horario_bp
from .usuarios import usuario_bp
from .productos import producto_bp
from .servicios_productos import servicio_producto_bp
from .proveedores_productos import proveedor_producto_bp
from .inventarios_movimientos import inventario_movimiento_bp
from .documentacion import documentacion_bp

def cargarRutas(app):
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(cita_bp, url_prefix='/citas')
    app.register_blueprint(detalle_cita_bp, url_prefix='/detalle_citas')
    app.register_blueprint(detalle_factura_bp, url_prefix='/detalle_facturas')
    app.register_blueprint(factura_bp, url_prefix='/facturas')
    app.register_blueprint(proveedor_bp, url_prefix='/proveedores')
    app.register_blueprint(servicio_bp, url_prefix='/servicios')
    app.register_blueprint(pago_bp, url_prefix='/pagos')
    app.register_blueprint(empleado_bp, url_prefix='/empleados')
    app.register_blueprint(horario_bp, url_prefix='/horarios')
    app.register_blueprint(usuario_bp, url_prefix='/usuarios')
    app.register_blueprint(producto_bp, url_prefix='/productos')
    app.register_blueprint(servicio_producto_bp, url_prefix='/servicios_productos')
    app.register_blueprint(proveedor_producto_bp, url_prefix='/proveedores_productos')
    app.register_blueprint(inventario_movimiento_bp, url_prefix='/inventario_movimientos')
    app.register_blueprint(documentacion_bp, url_prefix='/documentacion')
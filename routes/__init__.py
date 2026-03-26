from .cliente import cliente_bp

def cargarRutas(app):
    app.register_blueprint(cliente_bp, url_prefix='/cliente')

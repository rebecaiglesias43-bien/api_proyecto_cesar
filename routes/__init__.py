from .cliente import cliente_bp
# from .roles import roles_bp

def cargarRutas(app):
    app.register_blueprint(cliente_bp, url_prefix='/cliente')
    # app.register_blueprint(roles_bp, url_prefix='/roles')

from flask import Flask

def registrar_blueprints(app):
    from .routes.rotas_main import rotas_bp
    from .routes.rotas_admin import rotas_bp_admin
    app.register_blueprint(rotas_bp)
    app.register_blueprint(rotas_bp_admin)

def criar_app():
    app = Flask(__name__, instance_relative_config=False)
    
    app.config['SECRET_KEY'] = 'minha_palavra_secreta'

    # Chaves de sessão
    app.config["SESSION_USER_ID"] = "id_usuario"
    app.config["SESSION_USER_ROLE"] = "tipo_usuario"
    app.config["SESSION_USER_EMAIL"] = "email"

    #Registra Blueprints
    
    registrar_blueprints(app)
    
    # Se quiser centralizar mais blueprints:
    # from .outra_rota import outra_bp
    # app.register_blueprint(outra_bp, url_prefix="/outra")

    return app
    
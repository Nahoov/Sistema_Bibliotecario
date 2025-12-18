from flask import Flask

def registrar_blueprints(app):
    from .rotas_main import rotas_bp
    app.register_blueprint(rotas_bp)

def criar_app():
    app = Flask(__name__, instance_relative_config=False)
    
    app.config['SECRET_KEY'] = 'minha_palavra_secreta'

    #Registra Blueprints
    
    registrar_blueprints(app)
    
    # Se quiser centralizar mais blueprints:
    # from .outra_rota import outra_bp
    # app.register_blueprint(outra_bp, url_prefix="/outra")

    return app
    
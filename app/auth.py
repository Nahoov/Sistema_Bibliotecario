# Importa a função wraps, usada para preservar os metadados da função original quando criamos um decorator
from functools import wraps

from flask import session, redirect, url_for, flash, current_app
# session  -> armazena dados do usuário entre requisições
# flash -> envia mensagens temporárias para o usuário

# =========================
# DECORATOR: login_required
# =========================
# Este decorator garante que apenas usuários LOGADOS possam acessar a rota

def login_required(f):
    # wraps(f) mantém o nome e os metadados da função original
    @wraps(f)
    def wrapper(*args, **kwargs):

        user_id_key = current_app.config["SESSION_USER_ID"]

        # Verifica se NÃO existe 'id_usuario' na sessão
        # Se não existe, significa que o usuário não está logado
        if user_id_key not in session:
            flash('Faça login para acessar essa página.', "info")
            return redirect(url_for('rotas_main.pagina_login'))

        # Se o usuário estiver logado, a função original (rota) é executada normalmente
        return f(*args, **kwargs)

    # Retorna a função decorada
    return wrapper


# =========================
# DECORATOR: admin_required
# =========================
# Este decorator garante que apenas usuários ADMIN possam acessar a rota
def admin_required(f):
    @wraps(f)
    @login_required

    def wrapper(*args, **kwargs):

        # Segundo: verifica se o tipo de usuário NÃO é admin 
        # session.get() evita erro caso a chave não exista
        if session.get('tipo_usuario') != 'admin':
            flash('Acesso negado.', "warning")
            return redirect(url_for('rotas_main.pagina_user'))

        # Se o usuário estiver logado E for admin,
        # a função original é executada normalmente
        return f(*args, **kwargs)


    return wrapper

"""
"""


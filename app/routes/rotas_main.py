from flask import Blueprint, request, redirect, url_for, render_template, flash, current_app
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError
from psycopg2.extras import RealDictCursor
from ..conexao_banco import conecta_banco, encerra_conexao
from flask import session
from ..processar_dados import limpar_e_validar
from ..auth import login_required, admin_required


ph = PasswordHasher()

def iniciar_banco():

    global connection  
    global cursor 
    global cursorDict
  
    connection = conecta_banco()
    cursor = connection.cursor()
    cursorDict = connection.cursor(cursor_factory=RealDictCursor)

# ==================== ROTAS ==========================#

rotas_bp = Blueprint('rotas_main', __name__, url_prefix='/')

@rotas_bp.get('/')
def index():
    return render_template('index.html')


@rotas_bp.get('/login_biblioteca')
def pagina_login():
    return render_template('login.html')


@rotas_bp.get('/pagina_user')
@login_required
def pagina_user():
    return render_template('user.html')

@rotas_bp.get('/pagina_admin')
@admin_required
def pagina_admin():
        return render_template('admin.html')


@rotas_bp.post('/cadastrar')
def processar_cadastro():
    try:
        iniciar_banco()
        dados_processados = limpar_e_validar(request.form)

        if not dados_processados:
            return {"[ERROR": "Dados inválidos"}, 400


        query = """INSERT INTO usuarios (nome_usuario, sobrenome_usuario, email, data_nascimento, senha_hash) VALUES 
        (%s,%s,%s,%s,%s)"""

        cursor.execute(query, (dados_processados['nome'],
                               dados_processados['sobrenome'],
                               dados_processados['email'],
                               dados_processados['data_nascimento'],
                               dados_processados['senha_hash']))

        connection.commit()
        encerra_conexao(connection)

        print("<<<Dados enviados para o banco>>>")

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('rotas_main.pagina_login'), code=303)
    
    except Exception as e:
        return f"[ERROR - Final cadastro] | {e}", 500
    


@rotas_bp.post('/login')
def processar_login():

    iniciar_banco()
    email = (request.form.get('email') or '').strip()
    senha = (request.form.get('senha') or '').strip()

    if not email or not senha:
        flash('Email ou senha inválidos', "danger")
        flash('Teste info cayo en la primera no email o no senha', "info")
        flash('Teste warning', "warning")
        
        return redirect(url_for('rotas_main.pagina_login'))

    try:
        #with cursorDict:
        cursorDict.execute("SELECT email, senha_hash, tipo_usuario, id_usuario FROM usuarios WHERE email = %s", (email,))
        usuario = cursorDict.fetchone()

        if not usuario:
            flash('Email ou senha inválidos. not usuario', "danger")
            flash('Teste info', "info")
            flash('Teste warning', "warning")
            return redirect(url_for('rotas_main.pagina_login'))
        
    
        senha_hash = usuario['senha_hash']
        tipo_usuario = usuario['tipo_usuario']

        print("imprime tipo de usuario: ", tipo_usuario)

        ph.verify(senha_hash, senha)
        print("<< Senha válida >>")
        flash('Login efetuado!', "success")

        session[current_app.config["SESSION_USER_ID"]] = usuario["id_usuario"]
        session[current_app.config["SESSION_USER_ROLE"]] = tipo_usuario
        session[current_app.config["SESSION_USER_EMAIL"]] = usuario["email"]


        if tipo_usuario == 'admin':
            print("É admin")
            return redirect(url_for('rotas_main.pagina_admin'))
        
        else:
            return redirect(url_for('rotas_main.pagina_user'))
             
    #
    except (VerifyMismatchError, VerificationError):
            print(f"<<< Senha inválida >>>")
            flash('Email ou senha inválidos!', "danger")
            flash('Teste info cayo en el verify mismatch', "info")
            flash('Teste warning', "warning")
            return redirect(url_for('rotas_main.pagina_login'))
        
    
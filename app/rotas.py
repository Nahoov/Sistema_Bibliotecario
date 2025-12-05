from flask import Flask, request, redirect, url_for, render_template, flash
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHash
from psycopg2.extras import RealDictCursor
from conexao_banco import conecta_banco, encerra_conexao
from processar_dados import limpar_e_validar

app = Flask(__name__)

ph = PasswordHasher()

def iniciar_banco():

    global connection  
    global cursor 
    global cursorDict
  
    connection = conecta_banco()
    cursor = connection.cursor()
    cursorDict = connection.cursor(cursor_factory=RealDictCursor)


# ==================== ROTAS ==========================#
@app.get('/')
def index():
    return render_template('index.html')


@app.get('/login_biblioteca')
def pagina_login():
    return render_template('login.html')


@app.get('/pagina_user')
def pagina_user():
    return render_template('user.html')


@app.post('/cadastrar')
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
        print("Dados enviados!")

        return redirect(url_for('login_biblioteca'), code=303)
    
    except Exception as e:
        return f"[ERROR- Final cadastro] {e}", 500
    

@app.post('/login')
def processar_login():
    iniciar_banco()
    email = (request.form.get('email') or '').strip()
    senha = (request.form.get('senha') or '').strip()

    if not email or not senha:
        flash('Email ou senha inválidos.')
        return redirect(url_for('login_biblioteca'))
    
    try:
        with cursorDict:
                    cursorDict.execute("SELECT email, senha_hash FROM usuarios WHERE email = %s", (email,))
                    usuario = cursorDict.fetchone()

        if not usuario:
            flash('Email ou senha inválidos.')
            return redirect(url_for('login_biblioteca'))
        
    
        senha_hash = usuario['senha_hash']

        try:
            ph.verify(senha_hash, senha)
            print("<< Senha válida >>")
            return redirect(url_for('pagina_user'))
        
        except (VerifyMismatchError, VerificationError):
            print(f"<<< Senha inválida >>>")
            flash('Email ou senha inválidos.')
            return redirect(url_for('login_biblioteca'))

        

    except Exception as e:
        return print(f"[ERROR]: {e}")
from flask import Flask, request, redirect, url_for, render_template, flash
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHash
import re
from psycopg2.extras import RealDictCursor
from datetime import datetime
from argon2 import PasswordHasher
from conexao_banco import conecta_banco, encerra_conexao
from flask import current_app


app = Flask(__name__)

ph = PasswordHasher()

#connection = conecta_banco()
#cursor = connection.cursor()

#cursorDict = connection.cursor(cursor_factory=RealDictCursor)



#RE de regex - usada para validar se o email enviado no formulário tem um formato válido.
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

# Mensagens HTML simples (você pode personalizar/usar templates reais)
OK_HTML = """<h2>Cadastro realizado com sucesso!</h2><p><a href="/login.html">Ir para login</a></p>"""
ERROR_HTML = """<h2>Erro</h2><p>{{msg}}</p><p><a href="javascript:history.back()">Voltar</a></p>"""


def iniciar_banco():

    global connection  
    global cursor 
    global cursorDict
  
    connection = conecta_banco()
    cursor = connection.cursor()
    cursorDict = connection.cursor(cursor_factory=RealDictCursor)



def limpar_e_validar(form):
    nome = (form.get('nome') or '').strip()
    sobrenome = (form.get('sobrenome') or '').strip()
    email = (form.get('email') or '').strip()
    data_nascimento_raw = form.get('data_nascimento')  # espera YYYY-MM-DD do input type=date
    senha = form.get('senha')
    confirmar = form.get('confirmar_senha')

    # validações básicas
    if not nome or len(nome) < 2:
        return False, 'Nome inválido (mín 2 caracteres).', None
    
    if not sobrenome or len(sobrenome) < 2:
        return False, 'Sobrenome inválido (mín 2 caracteres).', None
    
    if not EMAIL_RE.match(email):
        return False, 'Email inválido.', None
    
    if not senha or len(senha) < 8:
        return False, 'Senha inválida (mín 8 caracteres).', None
    
    if senha != confirmar:
        return False, 'Senhas não coincidem.', None
    
    # validação data (opcional)
    data_nascimento = None
    if data_nascimento_raw:
        try:
            data_nascimento = datetime.strptime(data_nascimento_raw, '%Y-%m-%d').date()
        except ValueError:
            return False, 'Data de nascimento inválida (formato YYYY-MM-DD).', None
        
    try:
        senha_hash = ph.hash(senha) 
    except Exception as e:
        print(f"[ERROR] não foi possível criar senha | {e}")

    dic_limpo = {
        'nome': nome,
        'sobrenome': sobrenome,
        'email': email,
        'data_nascimento': data_nascimento,
        'senha_hash': senha_hash
    }

    return dic_limpo

 
    
# ===================== ROTAS =================#

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

    


# Execute este bloco APENAS se este arquivo for rodado diretamente.
# Não execute se ele for importado."
if __name__ == "__main__":
    # opção direta para desenvolvimento (não usar em produção)
    app.run(debug=True, host="127.0.0.1", port=8000)



   
